#!/usr/bin/env python

import os
assert os.uname()[0] != 'pyboard', "this code is not for a pyboard"

# Taking Screenshots
# on pyboard REPL:
#
#   >>> import lcd160cr
#   >>> isinstance(lcd, lcd160cr.LCD160CR)  # assuming lcd already exists
#   ... True
#   >>> from utils import screenshot
#   >>> screenshot(lcd, '/sd/screenshot.raw')  # saves .raw file to sd card
#
# Copy `screenshot.raw` from the sd card into this folder.
# In this folder...
#
#   $ ./convert.py
#   screenshot.raw > screenshot.png
#
# Now `screenshot.png` should exist in this folder


from glob import glob
from PIL import Image

X_DIM = 128
Y_DIM = 160

for filename_in in glob('*.raw'):
    # Output file (same name, different extension)
    filename_out = os.path.splitext(filename_in)[0] + '.png'
    print("%s > %s" % (filename_in, filename_out))

    with open(filename_in, 'rb') as fh:
        bytes = bytearray(fh.read())

        im = Image.new("RGB", (X_DIM, Y_DIM))
        for y in xrange(Y_DIM):
            for x in xrange(X_DIM):
                i = 2 * (x + (X_DIM * y))
                px = (bytes[i+1] << 8) + bytes[i]
                # the 255 is for the alpha channel which I plan to use later
                r = (px & 0x001F) << 3
                g = (px & 0x07E0) >> 3
                b = (px & 0xF800) >> 8
                im.putpixel((x, y), (r, g, b))

        im.save(filename_out, "PNG")
