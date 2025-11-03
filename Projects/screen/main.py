import requests
import time

from utils import wifi
from utils import wifiSecrets

#from machine import I2C

from screen.lcdSetup import screen
from screen.scrollUp import ScrollUp

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
# Saves lines after each example!
def clearLCD():
    time.sleep(3)
    screen.lcd.clear()




# Show a string on the LCD
screen().putstr("Hello, World!")


# This is how you move the cursor
# We moved it to the second row
# 1st number is column (X), 2nd number is row (Y)
# Numbers start at zero
# (0,0) is the 1st column, 1st row
screen.move_to(0, 1)
screen.putstr("Second row!")
clearLCD()

print("*********************************")
print("Display is now showing characters")
print("*********************************")


#for i in range(500): 
#    lcd.putstr("Count: " + str(i))
#    time.sleep(1)
#    lcd.clear()

# Run our function
#ScrollUp(str(quote))

crawl = (
    "A long time ago in a galaxy far, far away..."
    "Episode IV\nA NEW HOPE\n"
    "It is a period of civil war.\n"
    "Rebel spaceships, striking from a hidden base, have won their first victory..."
)

#ScrollUp(crawl, delay=0.5)