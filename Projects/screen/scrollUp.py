import time

def _rpad(s, w):
    # Right-pad with spaces without using str.ljust (MicroPython-safe)
    if len(s) < w:
        return s + (" " * (w - len(s)))
    return s[:w]

def _wrap16(text):
    """Yield 16-char chunks from a string."""
    for i in range(0, len(text), LCD_NUM_COLS):
        yield text[i:i+LCD_NUM_COLS]

def _prepare_lines(text_or_lines):
    """Normalize input to a flat list of 16-char lines, honoring newlines."""
    if isinstance(text_or_lines, str):
        parts = []
        for line in text_or_lines.splitlines():   # respects \n
            parts.extend(list(_wrap16(line)))
        return parts
    else:
        # assume list/iterable of lines; chunk any long ones
        parts = []
        for line in text_or_lines:
            parts.extend(list(_wrap16(line)))
        return parts

def ScrollUp(text, delay=0.4, clear_at_end=True):
    """
    Scroll text upward (Star Wars-style) on a 16x2 HD44780 once.
      - text: str (may include \n) or list of lines
      - lcd: I2cLcd instance
      - delay: seconds between steps
    """
    lines = _prepare_lines(text)

    # Add blank lines for smooth entry/exit
    pad = " " * LCD_NUM_COLS
    lines = [pad] + lines + [pad]

    total_steps = len(lines) - LCD_NUM_ROWS + 1
    for i in range(total_steps):
        line1 = _rpad(lines[i], LCD_NUM_COLS)
        line2 = _rpad(lines[i+1], LCD_NUM_COLS)

        lcd.move_to(0, 0); lcd.putstr(line1)
        lcd.move_to(0, 1); lcd.putstr(line2)
        time.sleep(delay)

    if clear_at_end:
        try:
            lcd.clear()
        except AttributeError:
            # Fallback clear if your driver lacks .clear()
            lcd.move_to(0, 0); lcd.putstr(pad)
            lcd.move_to(0, 1); lcd.putstr(pad)
