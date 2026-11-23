# 輸入輸出

來源：[lesson1](../sources/lesson1.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- `print(*objects, sep=" ", end="\n")`
  - 可以印很多個，中間預設空格隔開
  - 結尾預設換行
- `input("提示")` 讀進來一定是 str
  - 要數字就包起來：`depth = int(input("Enter depth: "))`

## 範例
```python
print("a", "b", "c", sep="-", end="!\n")
print(1, 2)
print("no newline", end="")
print(" <- same line")
```
```text
a-b-c!
1 2
no newline <- same line
```

## 常見錯誤
- 忘了轉型：`input()` 拿到 "3"，`"3" + 1` -> TypeError

## 相關頁
- [型別與轉換](types-and-casting.md)
