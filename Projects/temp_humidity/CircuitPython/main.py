import time
import board
import busio
import adafruit_ahtx0

# Use your actual wiring: SCL=GP17, SDA=GP16
i2c = busio.I2C(scl=board.GP17, sda=board.GP16)

# Just encase pins are different
while not i2c.try_lock():
    pass
print([hex(x) for x in i2c.scan()])
i2c.unlock()

sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)

#