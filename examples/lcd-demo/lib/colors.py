
def rgb24(val):
    return (
        (val >> 16) & 0xff,
        (val >> 8) & 0xff,
        (val >> 0) & 0xff,
    )

# Primaries
BLACK = rgb24(0x000000)
WHITE = rgb24(0xffffff)

RED = rgb24(0xff0000)
GREEN = rgb24(0x00ff00)
BLUE = rgb24(0x0000ff)

YELLOW = rgb24(0xffff00)
MAGENTA = rgb24(0xff00ff)
CYAN = rgb24(0x00ffff)

# Greys
GREY_10 = rgb24(0x191919)  # 10% grey
GREY_20 = rgb24(0x333333)  # 20% grey
GREY_30 = rgb24(0x4c4c4c)  # 30% grey
GREY_40 = rgb24(0x666666)  # 40% grey
GREY_50 = rgb24(0x7f7f7f)  # 50% grey
GREY_60 = rgb24(0x999999)  # 60% grey
GREY_70 = rgb24(0xb2b2b2)  # 70% grey
GREY_80 = rgb24(0xcccccc)  # 80% grey
GREY_90 = rgb24(0xe5e5e5)  # 90% grey
