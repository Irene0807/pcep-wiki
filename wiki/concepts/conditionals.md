# 條件判斷

來源：[lesson2](../sources/lesson2.md)、[tips](../sources/tips.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- `if` 條件 A：... `elif` 條件 B：... `else`：...
- 由上往下，第一個成立的就做，後面不看
- 條件後面一定要冒號，內容要縮排
- 比較相等用 `==`，`=` 是給值

## 範例
```python
score = 75
if score >= 90:
    print("A")
elif score >= 60:
    print("pass")
else:
    print("fail")
```
```text
pass
```

## 常見錯誤
- `if score = 60:` -> SyntaxError
- 忘了冒號、縮排不一致

## 相關頁
- [迴圈](loops.md)
- [運算子](operators.md)
