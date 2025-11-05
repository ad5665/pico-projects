from utils.wifi import connect, ensure_connected, ifconfig
from utils.wifiSecrets import *

# Connect tp Wi-Fi up
wlan = wifi.connect(wifiSecrets.WIFI_SSID, wifiSecrets.WIFI_PASS, hostname="pico-motion")
print("Wi-Fi:", wifi.ifconfig(wlan))