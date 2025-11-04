import requests
import time

from utils import wifi
from utils import wifiSecrets

from screen.lcdSetup import screen
from screen.scrollUp import ScrollUp
from screen.scrollLeft import ScrollLeft
from screen.scrollLeft2Lines import ScrollLeft2Lines

# Connect tp Wi-Fi up
wlan = wifi.connect(wifiSecrets.WIFI_SSID, wifiSecrets.WIFI_PASS, hostname="pico-motion")
print("Wi-Fi:", wifi.ifconfig(wlan))


# Make GET request
response = requests.get("https://api.quotable.io/random")
data = response.json()
# Get response code
response_code = response.status_code
# Get response content
response_content = response.content
quote = data["content"]

# Print results
print('Response code: ', response_code)
print('Response content:', quote)

# Just a function to sleep and then clear the LCD
def clearLCD():
    time.sleep(3)
    lcd.clear()


# instantiate the screen once
lcd = screen()

print("*********************************")
print("Display is now showing characters")
print("*********************************")

#ScrollLeft2Lines("BOOOOOOOO0000000000000000000")

# Run our function
ScrollUp(str(quote))

crawl = (
    "A long time ago in a galaxy far, far away..."
    "Episode IV\nA NEW HOPE\n"
    "It is a period of civil war.\n"
    "Rebel spaceships, striking from a hidden base, have won their first victory..."
)

ScrollUp(crawl, delay=0.5)