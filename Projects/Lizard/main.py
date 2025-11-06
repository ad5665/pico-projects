from machine import Pin
import time
import screen 

from utils import connect, ifconfig
from utils.wifiSecrets import WIFI_SSID, WIFI_PASS

wlan = connect(WIFI_SSID, WIFI_PASS, hostname="pico-test")
print("Wi-Fi:", ifconfig(wlan))

button = Pin(2, Pin.IN, Pin.PULL_DOWN)

crawl = (
    "IM A\n"
    "LIZARD\n"
    "BITCH"
)

# ----- IRQ-based press detection with debounce -----
_pressed = False
_last = time.ticks_ms()

def on_press(pin):
    global _pressed, _last
    now = time.ticks_ms()
    if time.ticks_diff(now, _last) > 200:   # 200 ms debounce
        _pressed = True
        _last = now

button.irq(trigger=Pin.IRQ_RISING, handler=on_press)

# Optional: clear once at start
screen.clearLCD()

while True:
    if _pressed:
        _pressed = False

        # Draw only when needed; don't clear every frame
        # Use a smaller delay so it feels responsive
        screen.ScrollUp(crawl, delay=0.1)   # tune this (0.02–0.1 usually feels good)

        # If ScrollUp is long & you want to catch presses during it,
        # modify ScrollUp to yield periodically or break on a flag.

    # Small idle sleep to yield CPU
    time.sleep_ms(10)

#while True:
#    #time.sleep(0.2)
#
#    if button.value() == 1:
#        screen.ScrollUp(crawl, delay=0.5)
#
#    screen.clearLCD()