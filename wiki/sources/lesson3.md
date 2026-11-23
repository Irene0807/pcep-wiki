# Lesson 3 資料集合

來源：[raw/PCEP_lesson3_only_key_point.pdf](../../raw/PCEP_lesson3_only_key_point.pdf) (20 頁)

## 重點
- 3.1 五種：string、list、tuple、dict、set，比 有序 / 可改 / 可重複
- 3.2 list：宣告、取用、修改、`append insert del remove pop sort sorted count`
  - 複製：`b = a` 同一份，`b = a[:]`、`b = a.copy()` 兩份
  - slicing、list comprehension、`in`、`enumerate`
- 3.3 tuple：不能改，單一個值要加逗號 `(1,)`，unpacking，可以當 dict 的 key
  - 特例：tuple 裡的 list 可以改
- 3.4 dict：`a["id"]` vs `a.get("id")` (沒有會回 None)、`keys values items`、`pop`
- 3.5 string：不能改，`upper strip replace split join` 都是回傳新字串

## 對到的觀念頁
- [資料集合比較](../concepts/collections.md)
- [list](../concepts/list.md)
- [tuple、dict、string](../concepts/tuple-dict-string.md)
