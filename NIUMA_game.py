import asyncio
import random
from telethon import TelegramClient
from telethon.errors import RPCError

# ==========================================
# ⚙️ 專門設定區 (CONFIG)
# ==========================================
CONFIG = {
    # Telegram API 憑證 (請至 https://my.telegram.org 申請)
    "API_ID": 12345678,
    "API_HASH": "124367697oijbgyuik270abd",
    "SESSION_NAME": "session",
    # 目標頻道與訊息設定
    # 提示：Channel ID 需要加上 -100 前綴
    "CHAT_ID": -1002929014166,
    "MESSAGE_ID": 722359,
    # 要點擊的按鈕文字 (支援部分匹配)
    "BUTTON_TEXT": "💥 放大招(300-免)",
    # 冷卻時間範圍（秒）
    "COOL_DOWN_MIN": 31,
    "COOL_DOWN_MAX": 35,
    # 是否開啟無限循環攻擊模式
    "AUTO_LOOP": True,
}

# ==========================================
# 🚀 主程式邏輯
# ==========================================
client = TelegramClient(
    CONFIG["SESSION_NAME"], CONFIG["API_ID"], CONFIG["API_HASH"]
)


async def perform_attack():
    try:
        # 取得目標訊息
        message = await client.get_messages(
            CONFIG["CHAT_ID"], ids=CONFIG["MESSAGE_ID"]
        )

        if not message:
            print(f"❌ 找不到訊息 ID: {CONFIG['MESSAGE_ID']}")
            return False

        # 尋找並點擊指定的按鈕
        print(f"🎯 正在嘗試點擊按鈕: [{CONFIG['BUTTON_TEXT']}]...")
        result = await message.click(text=CONFIG["BUTTON_TEXT"])

        # 顯示 Bot 回覆的快顯提示訊息 (如果有)
        if result and hasattr(result, "message"):
            print(f"💬 Bot 回應: {result.message}")
        else:
            print("✅ 按鈕觸發成功！")

        return True

    except RPCError as e:
        print(f"⚠️ Telegram API 錯誤: {e}")
        return False
    except Exception as e:
        print(f"❌ 發生未預期錯誤: {e}")
        return False


async def main():
    await client.start()
    print("🤖 腳本已成功啟動並登入！")

    while True:
        success = await perform_attack()

        if not CONFIG["AUTO_LOOP"]:
            break

        # 計算 31 ~ 35 秒之間的浮點數隨機冷卻，避免行為過於固定
        sleep_time = random.uniform(
            CONFIG["COOL_DOWN_MIN"], CONFIG["COOL_DOWN_MAX"]
        )
        print(f"⏳ 進入冷卻時間，等待 {sleep_time:.2f} 秒後執行下一次...\n")
        await asyncio.sleep(sleep_time)


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
