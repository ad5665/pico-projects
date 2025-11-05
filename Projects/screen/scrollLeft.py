import time
from screen.lcdSetup import screen
lcd = screen()

def ScrollLeft(text):
    # Adds 16 blank spaces after our string
    text = text + (16 * " ")
    while True:
        # Always start each loop at 0,0
        lcd.move_to(0, 0)
        # Show the first 16 characters of the string
        lcd.putstr(text[:16])
        # Scroll speed delay
        time.sleep(0.5)
        # Updates 'text' before the next loop
        # text[1:] removes the first character
        # + text[0] adds the first character to the end
        text = text[1:] + text[0]
        print(text)