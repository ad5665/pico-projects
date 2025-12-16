import screen 

from utils import connect, ifconfig
from utils.wifiSecrets import WIFI_SSID, WIFI_PASS

wlan = connect(WIFI_SSID, WIFI_PASS, hostname="pico-test")
print("Wi-Fi:", ifconfig(wlan))

#screen.lcd.putstr("Simples")

screen.ScrollUp("UP UP UP")

screen.clearLCD()