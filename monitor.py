import os
import shutil
import subprocess

def get_storage_info():
    # Termux me home directory ki storage check karne ke liye
    total, used, free = shutil.disk_usage(os.path.expanduser("~"))
    # Bytes ko GB me convert karne ke liye
    total_gb = total / (1024**3)
    used_gb = used / (1024**3)
    free_gb = free / (1024**3)
    return total_gb, used_gb, free_gb

def get_battery_info():
    try:
        # Termux-api agar install na ho toh alternative crash na ho
        result = subprocess.run(['termux-battery-status'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
    except:
        pass
    return "Termux-API not configuration or installed."

print("=========================================")
print("📊      TERMUX DEVICE MONITOR          📊")
print("=========================================")

total_gb, used_gb, free_gb = get_storage_info()
print(f"📁 Total Storage : {total_gb:.2f} GB")
print(f"⚠️ Used Storage  : {used_gb:.2f} GB")
print(f"✅ Free Storage  : {free_gb:.2f} GB")

print("=========================================")

