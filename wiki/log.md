# log

## 2026-11-23 討論 ingest 範圍
- 主題：PCEP Python 入門，接 HW9 的講義網站
- 從 `Teaching/PCEP/` 挑 7 份：course_introduction、lesson1-4 key point、tips、practice_test_1_ans
- 先列每份重點給我確認 -> OK 才開始寫
- 簡報題目定為「Python 零基礎入門」，照 4 個 Block 排

## 2026-11-23 ingest 7 份
- course-introduction、lesson1、lesson3、lesson4、practice-test-1：抽文字 OK
- lesson2：抽出來程式順序亂掉 (`print("Condition 1")` 跑到 `if` 前面) -> 看圖重組，範例跑過
- tips：抽出來中文全是亂碼，AI 本來要跳過中文 -> 我要它改成每頁轉圖片看，12 頁都讀得到
- 建 sources 7 頁、concepts 14 頁、index

## 2026-11-23 check wiki 第 1 輪
- `python3 tools/check.py wiki` -> 22 頁、17 段範例
- 錯 1：index 連到 log.md，但 log 還沒建
- 自己再看一次：3 個例子講義沒有 (`-2 ** 2`、`x = a.sort()`、`round`)，沒照規則標「補充」-> 補標

## 2026-11-23 做簡報
- 從 index 找頁 -> 列 24 頁大綱，每頁標 wiki 頁 -> 生成 `slides/index.html`

## 2026-11-23 check slides 第 1 輪
- 結果 all passed，但只查到 1 段程式
- 原因：輸出框加了 `hide` class，checker 的 regex 只認 `class="out"` -> 19 段被跳過還顯示通過
- 修 checker，多印「查了幾段」，數字不對就知道漏了

## 2026-11-23 check slides 第 2 輪
- slide 11 錯：`print(i, end=" ")` 實際輸出多一個尾巴空白，寫的輸出沒有
- 這段是簡報另外寫的，不是從 wiki 抄 -> 只重生 slide 11，改成 wiki 有的寫法
- 對照 wiki 看內容：slide 9 寫了「0.1 在二進位是無限小數」，wiki 沒有 -> 刪掉，換成 wiki 有的 round

## 2026-11-23 check slides 第 3 輪 (截圖)
- headless Chrome 截圖看
- slide 4：程式框壓到底下的來源連結 -> 改左右排
- slide 13：表格太高，程式框碰到底 -> 縮表格
- quiz 的程式框少下框線 -> 補
- 版面問題靠眼睛看會漏 -> checker 加版面檢查 (每頁量內容有沒有超過底部)

## 2026-11-23 check slides 第 4 輪
- 版面檢查第一次跑：舊版 slide 13 沒被抓到
- 原因：量的時候 Google 字型還沒載入，用到較小的預設字 -> 改成等字型載完再量
- 故意用舊版測：抓到 slide 13 -> 檢查可信

## 2026-11-23 最終
- `python3 tools/check.py all`
  - wiki：22 頁、17 段範例
  - slides：24 頁、20 段範例、4 題測驗、版面
  - all passed
