# 資料集合比較

來源：[lesson3](../sources/lesson3.md)、[course-introduction](../sources/course-introduction.md)

## 重點
- string `"hello"`：有序、不能改、可重複
- list `[1, 2, 2, 3]`：有序、可改、可重複
- tuple `(1, 2, 3)`：有序、不能改、可重複
- dict `{"id": 18, "age": 20}`：key 不能重複、value 可以，可改；用 key 取值
- set `{1, 2, 3}`：無序、可改、不能重複
- 有序 -> 可以用 index `[0]` 取、可以 slicing
- 不能改 (immutable) -> `a[0] = 100` 會 error

## 範例
```python
print({1, 2, 2, 3})
print("hello"[1], [1, 2, 3][-1], (1, 2, 3)[0])
d = {"id": 18, "age": 20}
print(d["age"])
```
```text
{1, 2, 3}
e 3 1
20
```

## 常見錯誤
- `"hello"[0] = "K"` -> TypeError
- `(1, 2)[0] = 5` -> TypeError

## 相關頁
- [list](list.md)
- [tuple、dict、string](tuple-dict-string.md)
