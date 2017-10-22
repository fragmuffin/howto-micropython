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
            if val:
                self.led.intensity(10)
            else:
                self.led.off()

    def __enter__(self):
        # save buffer
        self.set_led(True)
        self.buffer = bytearray(2 * self.lcd.w * self.lcd.h)
        self.lcd.screen_dump(self.buffer)
        self.set_led(False)
        return self.buffer

    def __exit__(self, *args):
        self.set_led(True)
        self.lcd.set_pos(0, 0)
        self.lcd.screen_load(self.buffer)
        self.set_led(False)


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
