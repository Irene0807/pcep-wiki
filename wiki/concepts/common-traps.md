# 新手常見陷阱

來源：[tips](../sources/tips.md)、[practice-test-1](../sources/practice-test-1.md)、[lesson1](../sources/lesson1.md)、[lesson3](../sources/lesson3.md)、[lesson4](../sources/lesson4.md)

## 重點
1. `0.1 + 0.2 != 0.3` -> [型別與轉換](types-and-casting.md)
2. `**` 由右到左、`/` 一定 float -> [運算子](operators.md)
3. `if a = b` 要寫 `==` -> [條件判斷](conditionals.md)
4. `b = a` 不是複製 -> [list](list.md)
5. index 超出 error，slicing 超出沒事 -> [list](list.md)
6. `(1)` 不是 tuple -> [tuple、dict、string](tuple-dict-string.md)
7. string 方法不會改原本的 -> [tuple、dict、string](tuple-dict-string.md)
8. keyword 參數寫在 positional 前面 -> [function](functions.md)
9. 函式裡 `+=` 外面的變數 -> [scope](scope.md)
10. `True` / `False` 首字大寫

## 範例
```python
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3)  # 補充:比較前先round
```
```text
False
True
```

## 相關頁
- [index](../index.md)
