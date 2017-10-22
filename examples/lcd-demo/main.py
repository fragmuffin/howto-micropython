import lcd160cr
import pyb
import time

import widgets
from colors import *
from utils import restore_framebuffer

lcd = lcd160cr.LCD160CR('XY')
lcd.set_pen(WHITE, BLACK)
lcd.erase()

# ------ Create Button instances -------
PAD = 4
COLS = 2
ROWS = 4
def create_button(i, j, label=""):
    return widgets.Button(
        lcd,
        x1=int(i * (lcd.w / COLS) + PAD),
        y1=int(j * (lcd.h / ROWS) + PAD),
        x2=int((i + 1) * (lcd.w / COLS) - PAD),
        y2=int((j + 1) * (lcd.h / ROWS) - PAD),
        label=label,
    )

# To illuminate LED's
btn_blue = create_button(0, 0, "Blue")
btn_yellow = create_button(0, 1, "Yellow")
btn_green = create_button(0, 2, "Green")
btn_red = create_button(0, 3, "Red")

# Other fun stuff
btn_jpg = create_button(1, 0, "JPG")

# ------ LED utilities -------
led_red = pyb.LED(1)
led_green = pyb.LED(2)
led_yellow = pyb.LED(3)
led_blue = pyb.LED(4)

def set_led(led, value):
    if value:
        led.on()
    else:
        led.off()

# ------ Displaying a JPEG -------
def demo_show_jpg():
    lcd.set_pen(WHITE, BLACK)
    lcd.erase()

    with open('/sd/images/uc-moorabbin.jpg', 'rb') as f:
        f.seek(0xffff)  # max size
        buf = bytearray(f.tell())
        f.seek(0)
        f.readinto(buf)
    lcd.set_pos(0, 0)
    lcd.jpeg(buf)


try:
    # ------ Loop forever -------
    # checking for button presses
    while True:
        touch_info = lcd.get_touch()
        set_led(led_blue, btn_blue.is_pressed(*touch_info))
        set_led(led_yellow, btn_yellow.is_pressed(*touch_info))
        set_led(led_green, btn_green.is_pressed(*touch_info))
        set_led(led_red, btn_red.is_pressed(*touch_info))

        if btn_jpg.is_pressed(*touch_info):
            # Display a JPG
            with restore_framebuffer(lcd):
                demo_show_jpg()
                # wait for applause
                time.sleep(5)
        time.sleep(0.05)
except KeyboardInterrupt:
    # User has connected a REPL and pressed Ctrl+C
    pass
