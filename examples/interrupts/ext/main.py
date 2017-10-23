import pyb
import machine

def callback(i):
    print("intr")

pin = machine.Pin(
    'SW', machine.Pin.IN, machine.Pin.PULL_UP
)
ext = pyb.ExtInt(
    pin,
    pyb.ExtInt.IRQ_FALLING,
    machine.Pin.PULL_UP,
    callback
)
