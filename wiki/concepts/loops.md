# 迴圈

來源：[lesson2](../sources/lesson2.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- `while 條件:` 條件成立就一直做，記得改變數，不然無窮迴圈
- `for i in range(...)`：
  - `range(5)` -> 0,1,2,3,4
  - `range(2, 5)` -> 2,3,4
  - `range(-2, 3, 2)` -> -2,0,2
- 取 list：`for i in range(len(a))` 用 index，或 `for item in a` 直接拿值
- 迴圈 `else`：正常跑完才進，被 break 就不會進
- `pass` 佔位不做事、`break` 跳出整個迴圈、`continue` 跳過這一輪

## 範例
```python
i = 0
while i < 3:
    print("=", end="")
    i += 1
else:
    print("@")

for item in ["a", "c", "r"]:
    if item == "c":
        continue
    print(item)

for item in ["a", "c", "r"]:
    if item == "c":
        break
    print(item)
else:
    print("not printed")
```
```text
===@
a
r
a
```

## 常見錯誤
- while 裡忘了 `i += 1` -> 無窮迴圈 (Practice 13)
- range 的結尾不包含

## 相關頁
- [條件判斷](conditionals.md)
- [list](list.md)
