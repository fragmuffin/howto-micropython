import pyb
import utime as time

# Setup timing to achieve target baud-rate
baud = 250000  # 25k
pclk1 = pyb.freq()[2]
(bs1, bs2) = (5, 8)
prescaler = int(pclk1 / (baud * (1 + bs1 + bs2)))

# Initialize CAN controller
extframe = False
can1 = pyb.CAN(1, pyb.CAN.NORMAL, extframe=extframe, prescaler=prescaler, bs1=bs1, bs2=bs2)
#can2 = pyb.CAN(2, pyb.CAN.NORMAL, extframe=extframe, prescaler=prescaler, bs1=bs1, bs2=bs2)

def can2rx_cb(bus, reason):
    print('cb2', bus, reason)

#can1.setfilter(0, pyb.CAN.LIST32, 0, (0x211, 0x212))

can1.setfilter(0, pyb.CAN.LIST16, 0, (0x211, 0x212, 0x213, 0x214))

#while not can1.any(0):
#    time.sleep(0.01)
#
#print(can1.recv(0))
