import time
import network

# Simple, robust Wi-Fi connector for Pico W
def connect(ssid, password, *, max_wait=20, hostname="pico-motion"):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Set a hostname so your DHCP lease is neat in your router/HA
    try:
        wlan.config(hostname=hostname)
    except Exception:
        pass  # older firmware may not support hostname

    if not wlan.isconnected():
        wlan.connect(ssid, password)

        # Wait for link + DHCP
        for _ in range(max_wait * 4):  # 250ms ticks
            if wlan.isconnected():
                break
            time.sleep(0.25)

    if not wlan.isconnected():
        raise RuntimeError("Wi-Fi connect timeout")

    return wlan

def ensure_connected(wlan, ssid, password):
    """Lightweight guard you can call in your loop before MQTT work."""
    if wlan and wlan.isconnected():
        return wlan
    return connect(ssid, password)

def ifconfig(wlan):
    return wlan.ifconfig() if wlan else None
