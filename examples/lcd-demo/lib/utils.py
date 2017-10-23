import framebuf
import pyb

# ------------ Font Utilities ------------
_font_heights = {
    0: 4,
    1: 6,
    2: 7,
    3: 11,
}

def font_height(index, scale=0):
    return _font_heights[index] * (scale + 1) + scale


# ------------ LED Utilities ------------
class LEDOnContext():
    def __init__(self, led, intensity=255):
        self.led = led
        self.intensity = intensity

    def __enter__(self):
        if self.led:
            self.led.intensity(self.intensity)
        return self.led

    def __exit__(self, *args):
        if self.led:
            self.led.off()


def led_on(*args, **kwargs):
    """
    Turn an LED on during context block
    example usage:
        with led_on(pyb.LED(1)):
            time.sleep(0.5)
    """
    return LEDOnContext(*args, **kwargs)


# ------------ LCD Utilities ------------
class RestoreFrameContext():
    def __init__(self, lcd, led=True):
        self.lcd = lcd
        self.buffer = None

        # use LED to show when frame buffering is occuring
        self.led = None
        if led:
            self.led = pyb.LED(3)

    def set_led(self, val):
        if self.led:
            self.led.intensity(10 if val else 0)

    def __enter__(self):
        # save buffer
        with led_on(self.led, intensity=10):
            self.buffer = bytearray(2 * self.lcd.w * self.lcd.h)
            self.lcd.screen_dump(self.buffer)
        return self.buffer

    def __exit__(self, *args):
        with led_on(self.led, intensity=10):
            self.lcd.set_pos(0, 0)
            self.lcd.screen_load(self.buffer)


def restore_framebuffer(*args, **kwargs):
    """
    Record and restore LCD's frame buffer after context block.
    example usage:
        with restore_framebuffer(lcd):
            lcd.erase()
            # repurpose display for a while
            time.sleep(1)
    :param lcd: lcd160cr.LCD160CR instance
    """
    return RestoreFrameContext(*args, **kwargs)


def screenshot(lcd, filename, led=True):
    # LED stuff
    led_pin = None
    if led:
        led_pin = pyb.LED(3)

    # Take screenshot, save to file
    with led_on(led_pin, intensity=10):
        buffer = bytearray(2 * lcd.w * lcd.h)
        lcd.screen_dump(buffer)
        with open(filename, 'wb') as fh:
            fh.write(buffer)
