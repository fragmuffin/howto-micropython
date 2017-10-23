import lcd160cr
import lcd160cr_test
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
#btn_accel = create_button(1, 1, "Accel")
btn_features = create_button(1, 2, "Features")
btn_mandel = create_button(1, 3, "Mandel")

if btn_blue.is_pressed():
    # Take screenshot
    # press "Blue" button while booting to take screenshot
    from utils import screenshot
    screenshot(lcd, '/sd/screenshots/lcd-demo.raw')

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


# ------ DEMO: Displaying a JPEG -------
def demo_show_jpg():
    with open('/sd/images/photo.jpg', 'rb') as f:
        buf = bytearray(f.read())
    lcd.set_pos(0, 0)
    lcd.jpeg(buf)


# ------ DEMO: Graph Accelerometer Values -------
def demo_graph_accel(duration=None):
    # TODO
    time.sleep(duration)


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
                time.sleep(5)

        #elif btn_accel.is_pressed(*touch_info):
        #    with restore_framebuffer(lcd):
        #        demo_graph_accel(10)

        elif btn_features.is_pressed(*touch_info):
            # Built-in Test - Features
            with restore_framebuffer(lcd):
                lcd160cr_test.test_features(lcd)

        elif btn_mandel.is_pressed(*touch_info):
            # Built-in Test - Mandel
            with restore_framebuffer(lcd):
                lcd160cr_test.test_mandel(lcd)
                time.sleep(5)

        time.sleep(0.05)

except KeyboardInterrupt:
    # User has connected a REPL and pressed Ctrl+C
    # Clear screen
    lcd.set_pen(RED, BLACK)
    lcd.erase()
    # Draw an X (clear indication that we should be back into the REPL)
    lcd.line(0, 0, lcd.w-1, lcd.h-1)
    lcd.line(0, lcd.h-1, lcd.w-1, 0)
