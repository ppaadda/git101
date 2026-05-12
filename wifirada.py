import pywifi
import time
from pywifi import const

def simple_wifi_scanner():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0] # เลือกใช้การ์ด WiFi ตัวหลัก

    print("--- เริ่มต้นการดักฟังสัญญาณ (Passive Scanning) ---")
    print(f"Interface: {iface.name()}\n")
    
    # สั่งให้การ์ด WiFi สแกน (Passive ฟัง Beacon Frames)
    iface.scan()
    time.sleep(2) # ให้เวลาการ์ดในการเก็บรวบรวมข้อมูลรอบตัว
    
    # ดึงผลลัพธ์ที่ได้จากการฟัง
    scan_results = iface.scan_results()

    # หัวข้อตาราง
    print(f"{'SSID (ชื่อ WiFi)':<25} | {'BSSID (MAC)':<20} | {'Signal (RSSI)':<10}")
    print("-" * 60)

    for network in scan_results:
        # network.signal คือค่า RSSI (ความแรงของสัญญาณ)
        print(f"{network.ssid:<25} | {network.bssid:<20} | {network.signal} dBm")

#=================================================
#main function
if __name__ == "__main__":
    simple_wifi_scanner()
    
    