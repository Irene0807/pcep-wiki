# 例外處理

來源：[lesson4](../sources/lesson4.md)、[tips](../sources/tips.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- 沒處理的 error -> 程式中斷、出現紅字 (考題叫 Unhandled exception)
- `try:` 放可能出錯的，`except 錯誤類型:` 出錯時做的
- try 裡錯了之後的行不會跑
- 只會進一個 except
- 常見類型：ZeroDivisionError、ValueError、TypeError、IndexError、KeyError、NameError

## 範例
```python
def safe_int(s):
    try:
        n = int(s)
        print("ok")
    except ValueError:
        n = 0
        print("not a number")
    return n

print(safe_int("12"))
print(safe_int("Hi"))

try:
    print(1 / 0)
except ValueError:
    print("value")
except ZeroDivisionError:
    print("Undefined")
```
```text
ok
12
not a number
0
Undefined
```

## 常見錯誤
- 考題看到 def 先檢查會不會 error

## 相關頁
- [function](functions.md)
- [新手常見陷阱](common-traps.md)
