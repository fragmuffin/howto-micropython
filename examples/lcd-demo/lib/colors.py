import lcd160cr

def rgb(val):
    return lcd160cr.LCD160CR.rgb(
        (val >> 16) & 0xff,  # red
        (val >> 8) & 0xff,  # green
        (val >> 0) & 0xff,  # blue
    )

# Primaries
BLACK = rgb(0x000000)
WHITE = rgb(0xffffff)

RED = rgb(0xff0000)
GREEN = rgb(0x00ff00)
BLUE = rgb(0x0000ff)

YELLOW = rgb(0xffff00)
MAGENTA = rgb(0xff00ff)
CYAN = rgb(0x00ffff)

# Greys
GREY_10 = rgb(0x191919)  # 10% grey
GREY_20 = rgb(0x333333)  # 20% grey
GREY_30 = rgb(0x4c4c4c)  # 30% grey
GREY_40 = rgb(0x666666)  # 40% grey
GREY_50 = rgb(0x7f7f7f)  # 50% grey
GREY_60 = rgb(0x999999)  # 60% grey
GREY_70 = rgb(0xb2b2b2)  # 70% grey
GREY_80 = rgb(0xcccccc)  # 80% grey
GREY_90 = rgb(0xe5e5e5)  # 90% grey
