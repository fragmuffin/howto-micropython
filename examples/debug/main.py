import pyb

led = pyb.LED(1)
sw = pyb.Switch()

while True:
    time.sleep(0.05)
    if sw.value():
        led.on()
    else:
        led.off()
