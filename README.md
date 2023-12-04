# camp2023-story-bot
Telegram story bot written in Python for SITCON Camp 2023

## 敘述
- SITCON Camp 2023 故事半自動推送機器人，使用本屆教學 `pyTelegramBotAPI` 以及 `poetry` 虛擬環境。

## Dependency
- Python >= 3.11
- poetry >= 1.5.1
- pyTelegramBotAPI >= 4.12.0

## Setup
### 安裝 poetry
- 安裝
```bash
$ curl -sSL https://install.python-poetry.org | python3 -
```

- 設定環境變數
```bash
$ echo 'export PATH="~/.local/bin:$PATH"' >> ~/.bashrc
```

- 重啟終端並測試
```bash
$ poetry --version
```

### 安裝專案套件
```bash
$ poetry install
```
或者可以自行初始化（請先刪除 `pyproject.toml`）
```bash
$ poetry init
```
設定虛擬環境，並透過 `poetry add` 增加所需套件。

### 開發與執行
- 需要啟動 poetry shell，方可編輯程式碼與執行：
```bash
$ poetry shell
```

## 使用方式
1. 將故事文檔轉為 JSON 格式，並參考 `story/` 內範例，拆分各章節為單一檔案（幾個章節至少要有幾個檔案）；需要注意，每個檔案最大不能超過 20 則訊息（20 個 key），若超過擇需要再拆分。
2. 若是傳送圖片，請將圖片（PNG 檔）放置在 `img/`，並將 `"note"` 的值改為 `yes`，`"story"` 填上圖片檔名；圖片限制請參考 [API 說明](https://core.telegram.org/bots/api#sendphoto)。
3. 將 `main.py` 內故事推送的 `commands` 填入 `story/` 中各個檔案的檔名（如第一章為 `ch1`……），有拆分的章節全部都要填入。
4. 依據流程新增 bot 及頻道後，將 bot token 及頻道的 `chat_id` 填入。
5. 傳送時，在 poetry shell 下執行 `main.py`，並在 bot 的聊天室輸入 `/{章節名稱}`，即可傳送。

## 注意事項
- 故事內文可以使用 Markdown V2 語法，詳細請參考[API 說明](https://core.telegram.org/bots/api#markdownv2-style)。
- 圖片傳送使用 `InputFile`（[說明](https://core.telegram.org/bots/api#inputfile)）。
- 如果在自己的機器上直接執行程式，可能會發生 time out，所以傳送完畢建議就中止執行。