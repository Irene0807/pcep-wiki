# 型別與轉換

來源：[lesson1](../sources/lesson1.md)、[tips](../sources/tips.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- 基本型別
  - bool：`True`、`False` (首字大寫)
  - int：`1000`、`-5`、`3_000_000_000` (底線只是好讀)
  - float：`25.5`、科學記號 `3e8`
  - str：`"hello"`
  - None：什麼都沒有
- 進位制：二進位 `0b11010`、八進位 `0o32`、十六進位 `0x1A`，都是 26
- 轉換
  - `int(3.6)` -> 3 (直接切掉，不四捨五入)
  - `int("12")` -> 12，`int("Hi")` -> error
  - `float(True)` -> 1.0
  - `str(12.5)` -> '12.5'
  - `bool(0)`、`bool("")` -> False，`bool(" ")` -> True (有空白就不是空的)
- float 不精準：用二進位存，只是很接近的值

## 範例
```python
print(type(3_000_000_000), 0b11010, 0o32, 0x1A)
print(int(3.6), float(True), str(12.5))
print(bool(0), bool(""), bool(" "))
print(0.1 + 0.2)
print("5" + "6", 5 + 6)
```
```text
<class 'int'> 26 26 26
3 1.0 12.5
False False True
0.30000000000000004
56 11
```

## 常見錯誤
- `float(TRUE)` -> NameError，要寫 `True`
- `int("Hi")` -> ValueError
- `"5" + 6` -> TypeError，字串和數字不能直接加

## 相關頁
- [輸入輸出](input-output.md)
- [運算子](operators.md)
