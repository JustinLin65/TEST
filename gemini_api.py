from google import genai

# ================= 填入區 =================
API_KEY = "YOUR_API_KEY_HERE"  # 請替換成你的 API Key
MODEL_NAME = "gemini-2.5-flash"
TEST_PROMPT = "ping"
# =========================================

def run_test():
    client = genai.Client(api_key=API_KEY)

    try:
        # --- 功能 A: 列出所有可用模型 ---
        print("--- 正在獲取可用模型清單 ---")
        model_list = client.models.list()
        
        found_flash = False
        for m in model_list:
            # 新版 SDK 使用 supported_actions (是一個 list)
            if 'generateContent' in m.supported_actions:
                print(f"可用模型: {m.name}")
                if "flash" in m.name:
                    found_flash = True
        
        if not found_flash:
            print("\n[提示] 清單中似乎沒有看到 flash 模型，請檢查 API Key 是否有對應權限。")
            
        print("\n" + "="*30 + "\n")

        # --- 功能 B: 測試內容生成 ---
        print(f"正在測試模型: {MODEL_NAME} ...")
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=TEST_PROMPT
        )
        
        print("--- 測試成功！ ---")
        print(f"AI 回覆內容：\n{response.text}")

    except Exception as e:
        print(f"\n[!] 發生錯誤：{e}")

if __name__ == "__main__":
    run_test()