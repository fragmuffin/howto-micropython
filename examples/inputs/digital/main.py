import machine

# Pin connected to pyboard's Switch
pin = machine.Pin('SW')
pin.names()  # ['B3', 'X17', 'SW']  alternatives

# The switch connects the B3 pin to GND when pressed
pin.value()  # 0 when pressed
             # 1 when not pressed
