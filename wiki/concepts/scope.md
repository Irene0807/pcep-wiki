# scope

來源：[lesson4](../sources/lesson4.md)、[tips](../sources/tips.md)、[practice-test-1](../sources/practice-test-1.md)

## 重點
- function 外面建的 -> global variable
- function 裡面建的 -> local variable
- 同名時 local 優先 (shadowing)
- 裡面改只影響裡面，要動外面要寫 `global`

## 範例
```python
num = 200
def only_read():
    print("inside", num)
only_read()

def local_one():
    num = 400
    print("inside", num)
local_one()
print("outside", num)

def use_global():
    global num
    num = 400
use_global()
print("outside", num)
```
```text
inside 200
inside 400
outside 200
outside 400
```

```python
def do_the_mess(parameter):
    variable += parameter[0]
    return variable

variable = -1
do_the_mess([2])
```
```text
UnboundLocalError
```

## 常見錯誤
- 函式裡 `+=` 外面的變數又沒寫 global -> UnboundLocalError (Practice 23)

## 相關頁
- [function](functions.md)
