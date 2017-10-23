import machine
import pyb

led = machine.Pin('LED_RED')
def toggle_led_cb(tim):
    led.value(1 - led.value())

timer = pyb.Timer(1, freq=1000)
timer.counter() # get counter value
timer.freq(2) # 2 Hz
timer.callback(toggle_led_cb)
