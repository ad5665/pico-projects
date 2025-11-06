#from utils.wifi import connect, ensure_connected, ifconfig
#from utils.wifiSecrets import *
#
## Connect tp Wi-Fi up
#wlan = wifi.connect(wifiSecrets.WIFI_SSID, wifiSecrets.WIFI_PASS, hostname="pico-motion")
#print("Wi-Fi:", wifi.ifconfig(wlan))

from .wifi import connect, ensure_connected, ifconfig
from .umail import SMTP
__all__ = ["connect", "ensure_connected", "ifconfig", "SMTP"]