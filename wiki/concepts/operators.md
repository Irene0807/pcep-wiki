# 運算子

來源：[lesson1](../sources/lesson1.md)、[tips](../sources/tips.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- 數學：`**` 次方、`*`、`/` (結果一定 float)、`//` 取商、`%` 取餘數、`+`、`-`
- 字串：`"a" + "b"` 接起來、`"a" * 3` 重複
- 比較：`== != > < >= <=`，結果是 bool
- 布林：`not`、`and` (兩個都 True)、`or` (一個 True 就好)
- 位元：`& | ^ ~ << >>`
- 優先級 (高 -> 低)
  - `()` 括號
  - `**`
  - 正負號 `+x -x`
  - `* / // %`
  - `+ -`
  - 比較
  - `not` -> `and` -> `or`
- 同一層由左到右，只有 `**` 由右到左

## 範例
```python
print(2 ** 3 ** 2)
print(10 * 3 / 2 % 2)
print(7 // 2, 7 % 2, 7 / 2)
print("a" * 3 + "b" * 2)
print(0b0011 & 0b0101, 0b0011 | 0b0101, 0b0011 ^ 0b0101)
print(not True or True and False)
```
```text
512
1.0
3 1 3.5
aaabb
1 7 6
False
```

## 常見錯誤
- `2 ** 3 ** 2` 是 `2 ** 9` 不是 `8 ** 2`
- (補充) `-2 ** 2` 是 -4 (`**` 比負號強)
- `/` 就算整除也是 float：`4 / 2` -> 2.0

## 相關頁
- [型別與轉換](types-and-casting.md)
- [條件判斷](conditionals.md)
