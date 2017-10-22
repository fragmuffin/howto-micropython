import lcd160cr
import pyb
import time

import widgets
from colors import *

lcd = lcd160cr.LCD160CR('XY')
lcd.set_pen(lcd.rgb(*WHITE), lcd.rgb(*BLACK))
lcd.erase()

PAD = 4
COLS = 2
ROWS = 4
def create_button(i, j):
    return widgets.Button(
        lcd,
        x1=int(i * (lcd.w / COLS) + PAD),
        y1=int(j * (lcd.h / ROWS) + PAD),
        x2=int((i + 1) * (lcd.w / COLS) - PAD),
        y2=int((j + 1) * (lcd.h / ROWS) - PAD),
    )

btn_red = create_button(0, 0)
btn_green = create_button(0, 1)
btn_yellow = create_button(0, 2)
btn_blue = create_button(0, 3)

led_red = pyb.LED(1)
led_green = pyb.LED(2)
led_yellow = pyb.LED(3)
led_blue = pyb.LED(4)

def set_led(led, value):
    if value:
        led.on()
    else:
        led.off()

try:
    while True:
        touch_info = lcd.get_touch()
        set_led(led_blue, btn_red.is_pressed(*touch_info))
        set_led(led_yellow, btn_green.is_pressed(*touch_info))
        set_led(led_green, btn_yellow.is_pressed(*touch_info))
        set_led(led_red, btn_blue.is_pressed(*touch_info))
        time.sleep(0.05)
except KeyboardInterrupt:
    # User has connected a REPL and pressed Ctrl+C
    pass

# just before repl
lcd.set_pen(0xffff, 0)
lcd.erase()

with open('/sd/images/test.jpg', 'rb') as f:
    f.seek(0xffff)  # max size
    buf = bytearray(f.tell())
    f.seek(0)
    f.readinto(buf)
lcd.set_pos(0, 0)
lcd.jpeg(buf)
