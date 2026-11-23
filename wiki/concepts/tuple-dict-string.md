# tuple、dict、string

來源：[lesson3](../sources/lesson3.md)、[tips](../sources/tips.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- tuple
  - 不能改，沒有 append / remove / sort
  - 只有一個值要加逗號：`(1,)` 或 `1,`
  - unpacking：`x, y = (3, 5)`
  - 可以當 dict 的 key
  - 特例：tuple 裡的 list 可以改
- dict
  - `a["id"]` 沒這個 key -> KeyError
  - `a.get("id")` 沒有回 None，比較安全
  - `keys()`、`values()`、`items()`
  - 加 / 改都是 `a["key"] = value`
- string
  - 不能改
  - `upper lower capitalize strip replace split join` 都回傳新字串，原本的不變

## 範例
```python
t = (10, [20, 30], 40)
t[1][1] = 25
print(t, type((1,)), type((1)))
x, y = (3, 5)
print(x, y)
d = {"id": 18}
print(d.get("age"))
s = "hello"
s.upper()
print(s, s.upper(), "-".join(["a", "b"]))
menu = {"chocolate": 3.21, "churros": 1.99}
for v in menu.values():
    print(str(v)[1], end="")
print()
```
```text
(10, [20, 25], 40) <class 'tuple'> <class 'int'>
3 5
None
hello HELLO a-b
..
```

## 常見錯誤
- `(1)` 不是 tuple，是 int
- `s.upper()` 沒接回來，s 還是小寫

## 相關頁
- [資料集合比較](collections.md)
- [list](list.md)
