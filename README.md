# Python 測試與工具腳本集 (TEST)

本專案包含數個用於環境檢測、API 測試以及輸入行為監聽的 Python 腳本。

## 檔案說明

### 1. Hello.py

* **用途**：基礎 Python 測試程式。
* **功能**：單純輸出 `Hello, World!`，用於快速檢查 Python 編譯器/直譯器是否能順利執行。

### 2. detection.py

* **用途**：Python 執行環境資訊檢測。
* **功能**：印出當前運行的 Python 版本與 Python 執行檔的實際路徑，便於排查多重 Python 環境的設定問題。

### 3. gemini_api.py

* **用途**：Google Gemini API 功能測試。
* **功能**：
  * 使用新版 `google-genai` SDK 進行身份驗證與呼叫。
  * 列出該 API Key 可用的所有 Gemini 模型清單。
  * 呼叫 `gemini-2.5-flash` 模型，傳送測試 Prompt 並印出 AI 的回覆內容，以確認 API 串接正常。

### 4. recorder.py

* **用途**：鍵盤與滑鼠事件活動監聽器。
* **功能**：
  * 使用 `pynput` 與 `pyautogui` 即時偵測使用者的滑鼠移動、點擊、滾輪捲動以及鍵盤按鍵輸入。
  * 將偵測到的詳細行為輸出至控制台（終端機），並同時寫入本地日誌檔 `input_log.txt` 中。
  * 按下鍵盤 `Esc` 鍵可立即安全地終止監聽。
