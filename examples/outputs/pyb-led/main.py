import pyb

red_led = pyb.LED(1)
yellow_led = pyb.LED(3)

# Basic controlls
red_led.on()
red_led.off()
red_led.toggle()

# Yellow and Blue have intensity control
yellow_led.intensity(0xff)  # same as on()
yellow_led.intensity(0x00)  # same as off()
