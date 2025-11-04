import time

from screen.lcdSetup import screen
from screen.scrollUp import ScrollUp
from screen.scrollLeft import ScrollLeft
from screen.scrollLeft2Lines import ScrollLeft2Lines

# Just a function to sleep and then clear the LCD
def clearLCD():
    time.sleep(3)
    lcd.clear()


# instantiate the screen once
lcd = screen()