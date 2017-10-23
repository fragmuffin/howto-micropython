import machine
import pyb

pin = machine.Pin('LED_BLUE')
timer = pyb.Timer(3, freq=1000)
channel = tim.channel(1, pyb.Timer.PWM, pin=pin)

# Change blue LED's intensity manually
channel.pulse_width_percent(5)
channel.pulse_width_percent(50)
channel.pulse_width_percent(100)
