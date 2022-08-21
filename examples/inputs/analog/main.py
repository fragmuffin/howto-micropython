import machine
import utime as time
import pyb

pin = machine.Pin('X19')
adc = pyb.ADC(pin)
adc.read()  # reads value, 0-4095

while True:
    time.sleep(0.1)
    value_ratio = adc.read() / 4095
    print('#' * int(40 * value_ratio))
