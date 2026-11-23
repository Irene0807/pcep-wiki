# 基本語法

來源：[lesson1](../sources/lesson1.md)

## 重點
- keywords 保留字不能當變數名，`keyword.iskeyword(s)` 可以查
- 一行一個指令 (instruction)
- 縮排決定程式區塊，PEP 8 建議 4 個空格
- 註解：`#`，整段選起來按 ctrl + /
- 變數命名
  - 只能有英文大小寫、數字、底線
  - 開頭不能是數字
  - 大小寫有差
  - 不能用 keywords
- PEP 8 (建議不強制)：變數小寫、常數全大寫 (`PI`、`MAX_SIZE`)、多個字用底線 (`max_size`)、class 字首大寫、等號和運算子左右空格

## 範例
```python
import keyword
print(keyword.iskeyword("for"), keyword.iskeyword("score"))
Score = 1
score = 2
print(Score, score)
```
```text
True False
1 2
```

## 常見錯誤
- `2name = 1` -> SyntaxError (數字開頭)
- `in = 3` -> SyntaxError (用到保留字)

## 相關頁
- [直譯與編譯](interpreter-compiler.md)
- [新手常見陷阱](common-traps.md)
