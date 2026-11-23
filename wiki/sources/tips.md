# PCEP 考前提醒

來源：[raw/PCEP_tips.pdf](../../raw/PCEP_tips.pdf) (12 頁)

## 重點
- L1-2
  - 只有 `**` 由右到左，其他運算都由左到右
  - if 裡比較用 `==`
  - `3_000_000_000` 是 int
- 英文單字：binary 二進位、interpreted / compiled 直譯 / 編譯、iterate 迭代、argument vs. parameter 引數 / 參數、position 位置
- L3
  - `list[5]` 超出範圍 -> IndexError，`list[3:5]` 切片超出沒關係
  - 複製：`a = b` 同一份，`b = a[:]`、`b = a.copy()` 兩份
- L4
  - 第四章 if 程式題，優先想會不會 error (= Unhandled exception)
  - 常見 error：該給的參數沒給 / 型別給錯、用到保留字 (in)、`+=` 用在還沒有值的變數
- 附 Practice 2、5、18、19、23、25、27 

## 對到的觀念頁
- [運算子](../concepts/operators.md)
- [list](../concepts/list.md)
- [function](../concepts/functions.md)
- [新手常見陷阱](../concepts/common-traps.md)

ps. 這份 PDF 抽文字中文全是亂碼，改成每頁轉圖片看
