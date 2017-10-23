import machine

pin = machine.Pin('SW', machine.Pin.IN, machine.Pin.PULL_UP)
pin = machine.Pin('SW', machine.Pin.IN, machine.Pin.PULL_DOWN)
pin = machine.Pin('SW', machine.Pin.IN, machine.Pin.PULL_NONE)

# These 2 initialize the pin in the same way
pin = machine.Pin('SW')  # defaults for SW are...
pin = machine.Pin('SW', machine.Pin.IN, machine.Pin.PULL_UP)
