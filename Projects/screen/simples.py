"""
lcd.putstr("Hello, World!")


# This is how you move the cursor
# We moved it to the second row
# 1st number is column (X), 2nd number is row (Y)
# Numbers start at zero
# (0,0) is the 1st column, 1st row
lcd.move_to(0, 1)
lcd.putstr("Second row!")
clearLCD()

#for i in range(500): 
#    lcd.putstr("Count: " + str(i))
#    time.sleep(1)
#    lcd.clear()

"""