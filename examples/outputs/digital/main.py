import machine

# Both yield the same pin instance
pin = machine.Pin('A13', machine.Pin.OUT)
pin = machine.Pin('LED_RED', machine.Pin.OUT)
pin.names()  # ['A13', 'LED_RED']  shows alternatives

# Changing pin's state
pin.high()  # or: pin.on()
pin.low()  # or: pin.off()
print(pin.value())  # prints 0
pin.value(1 - pin.value())  # toggles pin
