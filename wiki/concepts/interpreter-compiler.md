# 直譯與編譯

來源：[lesson1](../sources/lesson1.md)、[tips](../sources/tips.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- 寫好的程式 (source code) 要先翻譯成機器語言才能跑
- 直譯 interpreting：邊翻邊執行 -> Python
  - 寫完直接跑、好除錯、好跨平台
  - 每次跑都要翻，比較慢；錯誤跑到那行才發現
- 編譯 compilation：全部翻完變 .exe 再執行 -> C / C++
  - 跑得快
  - 編譯久、改了要重編、不好跨平台
- Python 預設的直譯器叫 CPython (用 C 寫的)
- 程式能跑要過三關
  - lexis 詞彙：每個字都是合法 token
  - syntax 語法：符合規則，例如 if 後面要有冒號
  - semantics 語意：有意義，例如不能數字 + 字串、不能除以 0

## 範例
直譯：前面的行會先跑完，錯在第 2 行才停
```python
print("first")
print(1 / 0)
print("never")
```
```text
first
ZeroDivisionError
```

## 常見錯誤
- 考題「Python 是哪一類語言」答 interpreted，不是 compiled
- 高階語言寫的程式叫 source code，不是 machine code

## 相關頁
- [基本語法](syntax-basics.md)
