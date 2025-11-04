import time
from screen.lcdSetup import screen
lcd = screen()

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

def ScrollLeft2Lines(text, delay=0.3):
    """
    Scroll text left across a 16x2 LCD once.
    - text: string to display
    - lcd: your I2cLcd instance
    - delay: scroll speed (seconds)
    """

    # Pad text with blanks so it scrolls smoothly off the screen
    padded = text + (" " * LCD_NUM_COLS * LCD_NUM_ROWS)

    # Total scroll length (enough to fully clear)
    for i in range(len(padded) - (LCD_NUM_COLS * LCD_NUM_ROWS) + 1):
        # Grab a window of 32 chars (2 lines × 16 chars)
        window = padded[i:i + (LCD_NUM_COLS * LCD_NUM_ROWS)]

        # Split it into two lines
        line1 = window[:LCD_NUM_COLS]
        line2 = window[LCD_NUM_COLS:LCD_NUM_COLS*2]

        # Move cursor to start
        lcd.move_to(0, 0)
        lcd.putstr(line1)
        lcd.move_to(0, 1)
        lcd.putstr(line2)

        time.sleep(delay)