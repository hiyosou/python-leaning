import os
file_path="./data/check_file.txt"
if os.path.exists(file_path):
    print("ファイルがあります！")
    size=os.path.getsize(file_path)
    print(f"ファイルサイズ: {size} バイト")
else:
    print("ファイルが見つかりません。")
