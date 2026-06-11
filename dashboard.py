import os
import sys
import time
import shutil
from datetime import datetime

def get_battery_info():
    try:
        status = os.popen("termux-battery-status").read()
        if "percentage" in status:
            import json
            data = json.loads(status)
            return f"{data['percentage']}% ({data['status']})"
    except:
        pass
    return "N/A"

def get_ram_info():
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
        total = int(lines[0].split()[1]) // 1024
        free = int(lines[1].split()[1]) // 1024
        used = total - free
        return f"{used}MB / {total}MB"
    except:
        return "N/A"

def draw_dashboard():
    while True:
        os.system('clear')
        columns, rows = shutil.get_terminal_size()
        print("=" * columns)
        print("⚡ TERMUX ADVANCED SYSTEM DASHBOARD ⚡".center(columns))
        print("=" * columns)
        print(f"📅 Date & Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".center(columns))
        print("-" * columns)
        print(f"🔋 Battery Status : {get_battery_info()}".center(columns))
        print(f"🧠 RAM Usage     : {get_ram_info()}".center(columns))
        print("=" * columns)
        print("\n[ Press CTRL + C to Exit Dashboard ]".center(columns))
        time.sleep(1)

if __name__ == "__main__":
    try:
        draw_dashboard()
    except KeyboardInterrupt:
        print("\n\nDashboard closed. Back to terminal!")
        sys.exit()
