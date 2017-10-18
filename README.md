# How to MicroPython
This repo is my journey learning MicroPython,  documented as a presentation

presentation can be seen here: https://fragmuffin.github.io/howto-micropython/

the content found here is very likely not unique, but making it is part of my journey...
selfish, I know, but I hope you get something out of it.


# Target Content

As I gather content, I'll put it here.

Then, as I format it as a presentation (link above), I'll delete these sections.
Ultimately this entire _Target Content_ section will be removed... that's my process.

## What is MicroPython

`MicroPython` is a low level OS, with Python interpreter for the following microcontrollers:
* Espressif ESP8266
* Espressif ESP32
* ([and more](http://micropython.org/download))

Although all you _need_ is one of the above microcontrollers, purpose-built boards
can be purchased.
* [pyboard](https://store.micropython.org) (what I'll be using)
* [WiPy](https://pycom.io/product/wipy/) (less peripherals, but integrated WiFi, very cool)

## Connecting and the REPL

Read Evaluate Print Loop (REPL)

* Connecting with serial

Depending on your OS, you'll need to find which com port your `pyboard` is
connected to, read
[this tutorial](https://docs.micropython.org/en/latest/pyboard/pyboard/tutorial/repl.html)
to learn how to do this on your OS.

for me, on `ubuntu` the connected serial devices can be seen with

```bash
$ ls -l /dev/serial/by-id
drwxr-xr-x 2 root root 60 Oct 18 10:52 ./
drwxr-xr-x 4 root root 80 Oct 18 10:52 ../
lrwxrwxrwx 1 root root 13 Oct 18 10:52 usb-MicroPython_Pyboard_Virtual_Comm_Port_in_FS_Mode_3976346C3436-if01 -> ../../ttyACM0
```

from this I can see my `pyboard` is connected via /dev/ttyACM0, but I can
essentially connect to theh `pyboard` by referencing it's serial number.

so using `picocom`...

```bash
$ picocom /dev/serial/by-id/*3976346C3436*
picocom v1.7

port is        : /dev/ttyACM0
flowcontrol    : none
baudrate is    : 9600
parity is      : none
databits are   : 8
escape is      : C-a
local echo is  : no
noinit is      : no
noreset is     : no
nolock is      : no
send_cmd is    : sz -vv
receive_cmd is : rz -vv
imap is        :
omap is        :
emap is        : crcrlf,delbs,

Terminal ready
```

Note, the first line in terminal never seems to work, just press `[enter]` and you should see

```
Traceback (most recent call last):
  File "<stdin>", line 1
SyntaxError: invalid syntax
>>>
```

**Firmware Version**

To see firmware version, either:

pressing `[Ctrl+D]` will issue a soft reset, and display startup info

```
PYB: sync filesystems
PYB: soft reboot
MicroPython v1.9.2 on 2017-08-23; PYBv1.1 with STM32F405RG
Type "help()" for more information.
```

alternatively, you can run the following in the REPL

```python
>>> import os
>>> os.uname()
(sysname='pyboard', nodename='pyboard', release='1.9.2', version='v1.9.2 on 2017-08-23', machine='PYBv1.1 with STM32F405RG')
>>> os.uname().release
'1.9.2'
```

## Basics, using built in modules

http://docs.micropython.org/en/v1.9.2/pyboard/library/index.html

File-system
* on-board
* sd-card

```python
>>> import os
>>> os.listdir('/')
['flash', 'sd']
>>> os.getcwd()
'/flash'
>>> os.listdir('.')
['main.py', 'pybcdc.inf', 'README.txt', 'boot.py']
```

Hot mounting SD card

```python
>>> import os, pyb
>>> os.umount('/sd')
>>> os.listdir('/')
['flash']
>>> os.mount(pyb.SD, '/sd')
>>> os.listdir('/')
['flash', 'sd']
```

If SD card is not connected `OSError` is raised:

```python
try:
    os.mount(pyb.SD, '/sd')
    print("SD card mounted successfully")
except OSError:
    print("Mounting failed")
```

**LEDs**

```python
red_led = pyb.LED(1)
green_led = pyb.LED(2)
yellow_led = pyb.LED(3)
blue_led = pyb.LED(4)

# Basic controlls
red_led.on()
red_led.off()
red_led.toggle()
red_led.toggle()

# LED's 3 & 4 have intensity control
yellow_led.intensity(0xff)  # same as on()
yellow_led.intensity(0x00)  # same as off()
```

* Digital IO
* ADC & DAC(s)


## Downloading Modules (and where to find them)



## Less Basic

with some downloaded modules

* LCD Fun:
    * LCD Display
        * Pixel
        * Line
        * Text
    * LCD's Resistive Touch
* Networking (?)
    * WiFi (?)
*

## Realtime Stuff

* Interrupts, triggered by
    * Timer(s)
    * Digital Input

## Multitasking?

is this possible?


## WiFi / Other Platforms

* WiPy : https://pycom.io/product/wipy/
*
