# main.py -- put your code here!
import machine
import pyb

led = pyb.LED(1)

# Timer to turn light off
timer = pyb.Timer(1, freq=1000)
timer.freq(20) # every 50ms
timer.callback(None)

def check_sw(t):
    if pin.value():
        led.off()
        timer.callback(None)

# Callback to turn LED on
def led_on(i):
    led.on()
    timer.callback(check_sw)

# External Interrupt on Switch
pin = machine.Pin(
    'SW', machine.Pin.IN, machine.Pin.PULL_UP
)
btn_down = pyb.ExtInt(
    pin,
    pyb.ExtInt.IRQ_FALLING,
    machine.Pin.PULL_UP,
    led_on
)
