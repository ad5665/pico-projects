import requests

from screen import *
# Import wifi
from utils import connect, ifconfig
from utils.wifiSecrets import WIFI_SSID, WIFI_PASS

wlan = connect(WIFI_SSID, WIFI_PASS, hostname="pico-screen")
print("Wi-Fi:", ifconfig(wlan))

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


print("*********************************")
print("Display is now showing characters")
print("*********************************")

ScrollLeft("BOOOOOOOO0000000000000000000")

# Run our function
ScrollUp(str(quote))

crawl = (
    "A long time ago in a galaxy far, far away..."
    "Episode IV\nA NEW HOPE\n"
    "It is a period of civil war.\n"
    "Rebel spaceships, striking from a hidden base, have won their first victory..."
)

ScrollUp(crawl, delay=0.5)