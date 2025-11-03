import time
from umqtt.simple import MQTTClient
from picozero import pico_led
from machine import Pin

#import wifi
import secrets
import wifi
from utils import wifiSecrets
CLIENT_ID = b"pico-motion" 

# Set up PIR sensor
pir = Pin(15, Pin.IN)

# Connect tp Wi-Fi up
wlan = wifi.connect(wifiSecrets.WIFI_SSID, wifiSecrets.WIFI_PASS, hostname="pico-motion")
print("Wi-Fi:", wifi.ifconfig(wlan))

# Connect to MQTT
client = MQTTClient(
    client_id=CLIENT_ID,
    server=secrets.MQTT_BROKER,
    port=getattr(secrets, "MQTT_PORT", 1883),
    user=getattr(secrets, "MQTT_USER", None),
    password=getattr(secrets, "MQTT_PASS", None),
    keepalive=60,
)
client.connect()
print("Connected to MQTT")

# Main loop
prev_state = 0
while True:
    # Keep Wi-Fi solid (handles AP blips)
    wlan = wifi.ensure_connected(wlan, wifiSecrets.WIFI_SSID, wifiSecrets.WIFI_PASS)

    state = pir.value()
    if state != prev_state:
        if state == 1:
            print("Motion detected!")
            pico_led.on()
            client.publish(MQTT_TOPIC, b"motion")
        else:
            print("Motion cleared")
            pico_led.off()
            client.publish(MQTT_TOPIC, b"clear")
        prev_state = state

    # Keep MQTT session alive
    try:
        client.ping()
    except Exception:
        # Quick reconnect path
        try:
            client.connect()
            client.publish(AVAIL_TOPIC, b"online", retain=True)
        except Exception as e:
            # If broker is down, don’t crash; retry next tick
            pass
    time.sleep(0.2)