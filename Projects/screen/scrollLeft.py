import time
from screen.lcd_api import LcdApi
from screen.pico_i2c_lcd import I2cLcd
import screen.lcdSetup as slcd

def ScrollLeft(text):
    # Adds 16 blank spaces after our string
    text = text + (16 * " ")
    while True:
        # Always start each loop at 0,0
        slcd.lcd.move_to(0, 0)
        # Show the first 16 characters of the string
        slcd.putstr(text[:16])
        # Scroll speed delay
        time.sleep(0.5)
        # Updates 'text' before the next loop
        # text[1:] removes the first character
        # + text[0] adds the first character to the end
        text = text[1:] + text[0]
        print(text)