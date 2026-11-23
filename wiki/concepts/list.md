# list

來源：[lesson3](../sources/lesson3.md)、[tips](../sources/tips.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- 取用 `a[0]`、`a[-1]` 最後一個；修改 `a[0] = 100`
- `sum max min len`
- 加：`append(x)` 加最後、`insert(i, x)` 插到 i
- 減：`del a[1]`、`remove(x)` 刪第一個 x、`pop()` 拿出最後一個
- 排序：`a.sort()` 改原本的、`sorted(a)` 回傳新的
- 複製
  - `b = a`：同一份，改 b 等於改 a
  - `b = a[:]`、`b = a.copy()`：兩份
- slicing `a[start:end:step]`，end 不包含
- index 超出範圍 -> IndexError，slicing 超出不會 error
- list comprehension：`[i * 2 for i in range(5)]`
- `enumerate(a)` 同時拿 index 和值

## 範例
```python
a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
print(a, c)
print(a[3:10], a[1:4:2])
print([i * 2 for i in range(5)])
for i, j in enumerate(["apple", "banana"]):
    print(i, j)
```
```text
[1, 2, 3, 4] [1, 2, 3]
[4] [2, 4]
[0, 2, 4, 6, 8]
0 apple
1 banana
```

```python
a = [1, 2, 3]
print(a[5])
```
```text
IndexError
```

## 常見錯誤
- 以為 `b = a` 是複製
- (補充) `x = a.sort()` 拿到 None，sort 是改原本的

## 相關頁
- [資料集合比較](collections.md)
- [迴圈](loops.md)
- [新手常見陷阱](common-traps.md)
