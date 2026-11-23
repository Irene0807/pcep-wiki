import re, sys, subprocess, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
problems = []


def run(code, expect, where):
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=10)
    expect = expect.strip()
    err = re.match(r"^(\w+Error)$", expect.splitlines()[-1]) if expect else None
    if err:
        got = (r.stderr.strip().splitlines() or [""])[-1].split(":")[0]
        if got != err.group(1):
            problems.append(f"{where}: expect {err.group(1)}, got {got or 'no error'}")
        lines = expect.splitlines()[:-1]
        if lines and r.stdout.strip() != "\n".join(lines):
            problems.append(f"{where}: output before error\n  expect {lines}\n  got    {r.stdout.strip().splitlines()}")
    elif r.returncode != 0:
        problems.append(f"{where}: crashed -> {r.stderr.strip().splitlines()[-1]}")
    elif r.stdout.strip() != expect:
        problems.append(f"{where}: output wrong\n  expect {expect!r}\n  got    {r.stdout.strip()!r}")


def check_wiki():
    pages = sorted(WIKI.rglob("*.md"))
    index = (WIKI / "index.md").read_text()
    n_code = 0
    for p in pages:
        rel = p.relative_to(WIKI)
        text = p.read_text()
        for link in re.findall(r"\]\(([^)#]+\.(?:md|pdf))\)", text):
            if not (p.parent / link).resolve().exists():
                problems.append(f"{rel}: broken link {link}")
        if rel.parts[0] in ("sources", "concepts"):
            if not text.splitlines()[2].startswith("來源："):
                problems.append(f"{rel}: no source line")
            if str(rel) not in index:
                problems.append(f"{rel}: not in index")
        if rel.parts[0] == "concepts" and "../sources/" not in text.splitlines()[2]:
            problems.append(f"{rel}: concept not linked to any source")
        for i, (code, out) in enumerate(re.findall(r"```python\n(.*?)```\n```text\n(.*?)```", text, re.S)):
            n_code += 1
            run(code, out, f"{rel} code#{i+1}")
    print(f"wiki: {len(pages)} pages, {n_code} code blocks")


def check_slides():
    doc = (ROOT / "slides" / "index.html").read_text()
    slides = re.findall(r"<section(.*?)>(.*?)</section>", doc, re.S)
    n_code = n_quiz = 0
    for k, (attrs, body) in enumerate(slides, 1):
        src = re.search(r'data-src="([^"]*)"', attrs)
        if not src:
            problems.append(f"slide {k}: no data-src")
            continue
        for s in src.group(1).split():
            if not (WIKI / s).exists():
                problems.append(f"slide {k}: data-src {s} not found")
        for i, (code, out) in enumerate(re.findall(r'<pre class="code">(.*?)</pre>\s*<pre class="out[^"]*">(.*?)</pre>', body, re.S)):
            n_code += 1
            clean = lambda t: html.unescape(re.sub(r"<[^>]+>", "", t))
            run(clean(code), clean(out), f"slide {k} code#{i+1}")
        for q in re.findall(r'<div class="quiz" data-answer="(\w)" data-check="(.*?)">', body, re.S):
            ans, code = q
            n_quiz += 1
            r = subprocess.run([sys.executable, "-c", html.unescape(code)], capture_output=True, text=True)
            opts = dict(re.findall(r'<li data-key="(\w)">(.*?)</li>', body))
            got = r.stdout.strip() if r.returncode == 0 else "Unhandled exception"
            if html.unescape(re.sub(r"<[^>]+>", "", opts.get(ans, ""))) != got:
                problems.append(f"slide {k} quiz: answer {ans}={opts.get(ans)!r}, python says {got!r}")
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    url = (ROOT / "slides" / "index.html").as_uri() + "?check"
    dom = subprocess.run([chrome, "--headless=new", "--disable-gpu", "--window-size=1340,780",
                          "--virtual-time-budget=8000", "--dump-dom", url], capture_output=True, text=True).stdout
    flags = re.findall(r'<section[^>]*data-overflow="(\w+)"', dom)
    if len(flags) != len(slides):
        problems.append("layout check did not run")
    for k, f in enumerate(flags, 1):
        if f == "yes":
            problems.append(f"slide {k}: content overflows into footer")
    print(f"slides: {len(slides)} slides, {n_code} code blocks, {n_quiz} quiz, layout checked")


target = sys.argv[1] if len(sys.argv) > 1 else "all"
if target in ("wiki", "all"):
    check_wiki()
if target in ("slides", "all"):
    check_slides()
print("\n".join(problems) if problems else "all passed")
sys.exit(1 if problems else 0)
