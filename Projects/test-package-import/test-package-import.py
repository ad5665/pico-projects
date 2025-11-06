import screen 

from utils import connect, ifconfig
from utils.wifiSecrets import WIFI_SSID, WIFI_PASS

wlan = connect(WIFI_SSID, WIFI_PASS, hostname="pico-temp")
print("Wi-Fi:", ifconfig(wlan))

#screen.lcd.putstr("Simples")

screen.ScrollUp("STOP BE SUCH A NERD ALEX, GOD DAMMIT IM A NOOB")

screen.clearLCD()