from screen.lcd_api import LcdApi
from screen.pico_i2c_lcd import I2cLcd
import machine
from machine import I2C

# Define LCD I2C pins/BUS/address
SDA = 14
SCL = 15
I2C_BUS = 1
LCD_ADDR = 0x27

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

_lcd = None

def screen():
    global _lcd
    if _lcd is None:
        lcdi2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
        _lcd = I2cLcd(lcdi2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)
    return _lcd

#def screen():
#    # Set up LCD I2C
#    lcdi2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
#    print("BEFORE SETUP")
#    lcd = I2cLcd(lcdi2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)
#    print("AFTER SETUP")
#    return lcd