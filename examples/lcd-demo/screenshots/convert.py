#!/usr/bin/env python

import os
assert os.uname()[0] != 'pyboard', "this code is not for a pyboard"

from glob import glob
from PIL import Image

for filename_in in glob('*.raw'):
    filename_out = os.path.splitext(filename_in)[0] + '.png'
    print("%s > %s" % (filename_in, filename_out))
    with open(filename_in, 'rb') as fh:
        bytes = bytearray(fh.read())

        (X_DIM, Y_DIM) = (128, 160)
        (R, G, B) = (0, 0, 0)
        im = Image.new("RGB", (X_DIM, Y_DIM))
        for y in xrange(Y_DIM):
            for x in xrange(X_DIM):
                i = 2 * (x + (X_DIM * y))
                px = (bytes[i+1] << 8) + bytes[i]
                # the 255 is for the alpha channel which I plan to use later
                r = (px & 0x001F) << 3
                g = (px & 0x07E0) >> 3
                b = (px & 0xF800) >> 8
                if r > R: R = r
                if g > G: G = g
                if b > B: B = b
                im.putpixel((x, y), (r, g, b))

        print((R, G, B))
        im.save(filename_out, "PNG")
