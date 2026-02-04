import sys
import platform

# 基本輸出
print("Hello, World!")

# 顯示你的 Python 資訊
print("-" * 30)
print(f"Python 版本: {platform.python_version()}")
print(f"執行檔路徑: {sys.executable}")
print("-" * 30)

print("測試成功！你的 Python 環境運作正常。")