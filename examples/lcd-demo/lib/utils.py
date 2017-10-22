import framebuf


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
    def __init__(self, lcd):
        self.lcd = lcd
        self.buffer = None

    def __enter__(self):
        # save buffer
        self.buffer = bytearray(2 * self.lcd.w * self.lcd.h)
        self.lcd.screen_dump(self.buffer)
        return self.buffer

    def __exit__(self, *args):
        self.lcd.set_pos(0, 0)
        self.lcd.screen_load(self.buffer)


def restore_framebuffer(lcd):
    """
    Record and restore LCD's frame buffer after context block.
    example usage:
        with restore_framebuffer(lcd):
            lcd.erase()
            # repurpose display for a while
            time.sleep(1)
    :param lcd: lcd160cr.LCD160CR instance
    """
    return RestoreFrameContext(lcd)
