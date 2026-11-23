# PCEP Python Wiki

我的 PCEP 講義整理成的 LLM Wiki，AI 照這份規則 ingest、查詢、做簡報

## 資料夾

```
pcep-wiki/
├── raw/              # 原始講義 PDF，只讀不改
├── wiki/
│   ├── index.md      # 所有頁面清單，每頁一行
│   ├── log.md        # 每次 ingest / 檢查的紀錄
│   ├── sources/      # 一份 raw 一頁摘要
│   └── concepts/     # 觀念頁，跨多份來源
├── slides/index.html # 教學簡報
└── tools/check.py    # 檢查程式
```

## ingest 一份資料

1. 讀 raw 檔
   - 先抽文字，中文變亂碼或程式順序跑掉 -> 改成轉圖片看
2. 列 3-5 個重點給我確認，談好再寫 (先討論後生成)
3. 寫 `sources/<檔名>.md`
4. 更新或新增相關 `concepts/` 頁
   - 新內容跟舊頁矛盾 -> 不要直接蓋掉，兩個都留，標「待確認」問我
5. 程式範例用 `python3` 跑過，輸出寫在下面
6. 更新 `index.md`，在 `log.md` 加一筆
7. 跑 `python3 tools/check.py wiki`，沒過就回第 4 步

## 頁面格式

- 第一行 `# 標題`，第二行 `來源：` 接 sources 連結
- 觀念頁固定：重點 -> 範例 -> 常見錯誤 -> 相關頁
- 程式範例寫成 ```python，輸出寫成 ```text，緊接在後面
- 連結用相對路徑 `[list](list.md)`，不用 `[[ ]]`
- 只寫 raw 裡有的東西，raw 沒有的補充要標「補充」

## 查詢 / 做簡報

1. 先看 `index.md` 找相關頁，再讀頁面，不直接讀 raw
2. 列大綱，每頁標要用哪幾個 wiki 頁
3. 檢查大綱：4 個 Block 都有、順序由淺到深、沒有 wiki 沒寫的東西
4. 生成投影片
   - 每頁 `data-src` 填 wiki 頁路徑
   - 範例程式從 wiki 頁直接拿 (ingest 時已經跑過)，不要另外寫新的
   - 每句話都要在 data-src 那頁找得到
   - 範例程式用 `<pre class="code">` + `<pre class="out">`
5. 跑 `python3 tools/check.py slides`，哪頁沒過就只重生那頁
6. 結果記進 `log.md`

## 檢查程式在查什麼

- wiki：斷掉的連結、沒標來源的頁、沒進 index 的頁、python 範例跑出來跟寫的輸出不一樣
- slides：`data-src` 指到不存在的頁、範例輸出不對、測驗答案跟 python 跑的不一樣、內容超出頁面底部
- 看結果時先看「查了幾段」對不對，數字少了 = checker 漏抓，不是真的通過
- 新加一種檢查 -> 先拿故意弄壞的版本測，確定抓得到再用
