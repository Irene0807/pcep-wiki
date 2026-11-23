# function

來源：[lesson4](../sources/lesson4.md)、[tips](../sources/tips.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- 先定義 `def name(...):` 再呼叫 `name(...)`
- 好處：不用重複寫、好改 (改一個地方)、好讀 (可以分工)
- 傳進去：argument 引數 (外面)、parameter 參數 (裡面)
- 傳出來：`return` 回傳值，沒寫 return -> None
- 參數種類
  - required：一定要給，沒給 error
  - default：`name="Guest"`，沒給就用預設
  - positional：照位置對
  - keyword：`age=20`，順序無關
  - 混用時 positional 要在 keyword 前面
- recursion：function 裡呼叫自己，要有停下來的條件

## 範例
```python
def calculate_total(price):
    tax = price * 0.05
    return price + tax

def greet(name="Guest"):
    print("Hello", name)

def no_return():
    x = 1

print(calculate_total(100))
greet()
greet(name="Irene")
print(no_return())

def countdown(n):
    if n == 0:
        print("Done")
    else:
        print(n)
        countdown(n - 1)

countdown(2)
```
```text
105.0
Hello Guest
Hello Irene
None
2
1
Done
```

```python
def runner(brand, model="", year=2021):
    return brand + model
print(runner(model="Reluctance", 2019))
```
```text
SyntaxError
```

## 常見錯誤
- 該給的參數沒給 -> TypeError
- keyword 寫在 positional 前面 -> SyntaxError (Practice 27)

## 相關頁
- [scope](scope.md)
- [例外處理](exceptions.md)
