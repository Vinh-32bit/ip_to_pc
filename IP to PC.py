import subprocess
import os
import shutil
import tkinter as tk
from tkinter import messagebox

def run_powershell_command(command):
    try:
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Kết quả:")
            print(result.stdout)
        else:
            print("Lỗi:")
            print(result.stderr)
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def remove_folders_keep_files(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            for sub_item in os.listdir(item_path):
                sub_item_path = os.path.join(item_path, sub_item)
                if os.path.isfile(sub_item_path):
                    destination_path = os.path.join(directory, sub_item)

                    if os.path.exists(destination_path):
                        print(f"Tệp đã tồn tại: {destination_path}. Đang thêm số đếm vào tên tệp.")
                        base, extension = os.path.splitext(sub_item)
                        count = 1
                        while os.path.exists(destination_path):
                            destination_path = os.path.join(directory, f"{base}_{count}{extension}")
                            count += 1
                    shutil.copy2(sub_item_path, destination_path)
                    print(f"Đã sao chép tệp: {sub_item_path} vào {destination_path}")
            shutil.rmtree(item_path)
            print(f"Đã xóa thư mục: {item_path}")
            
if __name__ == "__main__":
    print("Made by Ngài Vinh")
    command = "python \"D:\Code\copyImage_Iphone\" \"This PC\Apple iPhone\Internal Storage\DCIM\" \"C:\Iphone_copy\" "
    directory = "C:\Iphone_copy"
    run_powershell_command(command)
    remove_folders_keep_files(directory)
    
    messagebox.showinfo("Ngài Vinh thông báo", "Ảnh và video được lưu ở thư mục Iphone_copy trong ổ C"
                        "\n\n C:\Iphone_copy "
                        "\n\n Bấm ok để mở")
    subprocess.Popen(f'explorer "{directory}"', shell=True)