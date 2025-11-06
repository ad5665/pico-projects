from machine import Pin
import time
import screen 

from utils import connect, ifconfig, SMTP
from utils.wifiSecrets import WIFI_SSID, WIFI_PASS
from utils.smtpSecrets import SMTP_HOST, SMTP_USER, SMTP_PASS, SMTP_TO

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

        # Send the email
        smtp = SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port

        try:
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.to(SMTP_TO)
            smtp.write("From:" + SMTP_USER + "<"+ SMTP_USER+">\n")
            smtp.write("Subject: Lizard\n")
            smtp.write(crawl)
            smtp.send()
            print("Email Sent Successfully")
        
        except Exception as e:
            print("Failed to send email:", e)
        finally:
            smtp.quit()

        screen.ScrollUp(crawl, delay=0.1)

    # Small idle sleep to yield CPU
    time.sleep_ms(10)
