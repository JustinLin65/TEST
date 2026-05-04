import pyautogui
from pynput import mouse, keyboard
import logging
import threading
import time

# 設定日誌格式，將偵測到的行為記錄下來
logging.basicConfig(
    filename="input_log.txt", 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
)

print("--- 滑鼠與鍵盤行為偵測程式已啟動 ---")
print("1. 所有活動將顯示在控制台並記錄至 'input_log.txt'")
print("2. 按下 'Esc' 鍵可停止程式")
print("-" * 40)

# 取得螢幕解析度 (使用 PyAutoGUI)
screen_width, screen_height = pyautogui.size()
print(f"目前螢幕解析度: {screen_width}x{screen_height}")

def on_move(x, y):
    # 這裡可以捕捉滑鼠移動，但因為移動太頻繁，通常不建議直接印出
    # logging.info(f"滑鼠移動至: ({x}, {y})")
    pass

def on_click(x, y, button, pressed):
    action = "按下" if pressed else "放開"
    msg = f"滑鼠 {button} {action} 於位置 ({x}, {y})"
    print(msg)
    logging.info(msg)

def on_scroll(x, y, dx, dy):
    direction = "向下" if dy < 0 else "向上"
    msg = f"滑鼠 {direction} 滾動 於位置 ({x}, {y})"
    print(msg)
    logging.info(msg)

def on_press(key):
    try:
        msg = f"鍵盤按下: {key.char}"
    except AttributeError:
        msg = f"功能鍵按下: {key}"
    
    print(msg)
    logging.info(msg)

def on_release(key):
    # 如果按下 Esc 則停止所有監聽
    if key == keyboard.Key.esc:
        print("\n偵測到 Esc 鍵，正在關閉程式...")
        return False

# 啟動滑鼠監聽
mouse_listener = mouse.Listener(
    on_move=on_move, 
    on_click=on_click, 
    on_scroll=on_scroll
)

# 啟動鍵盤監聽
keyboard_listener = keyboard.Listener(
    on_press=on_press, 
    on_release=on_release
)

# 使用線程執行監聽
mouse_listener.start()
keyboard_listener.start()

try:
    # 保持主程式運行，直到監聽器停止
    mouse_listener.join()
    keyboard_listener.join()
except KeyboardInterrupt:
    print("\n程式已手動中斷。")
finally:
    print("偵測已結束。日誌已儲存於 input_log.txt")