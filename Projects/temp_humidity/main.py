from machine import I2C, Pin
import time

from temp_humidity import aht20

from utils import connect, ifconfig
from utils.wifiSecrets import WIFI_SSID, WIFI_PASS

wlan = connect(WIFI_SSID, WIFI_PASS, hostname="pico-temp")
print("Wi-Fi:", ifconfig(wlan))

# --- Example usage on Pico W: GP16=SDA, GP17=SCL ---
i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
sensor = aht20.AHT20(i2c)

while True:
    t, h = sensor.read()
    print(f"T={t:.1f}C  RH={h:.1f}%")
    time.sleep(2)
