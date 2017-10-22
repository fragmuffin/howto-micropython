# Examples

These examples exhibit some or all functionality shown in the slides.


## Examples are for pyboard

These examples have only been tested on `pyboard` v1.1.

Furthermore: any examples that `import pyb` probably won't work on anything else.


# Running an example

Copy the entire contents of an example folder onto a blank micro SD card.

Put the micro SD card into the `pyboard`, and hit the reset button.

If you want to see `print` outputs, connect to a `REPL` and press `[Ctrl+D]`
to perform a soft reset.
You should be able to see `print` outputs right from the beginning of execution.

## Using `sync-to-sd.sh`

The `sync-to-sd.sh` script synchronises the content of a folder onto the SD card
currently plugged in to the `pyboard`.

This is only designed to be used from a linux environment (I'm running ubuntu).

You may be able to use a Raspberry Pi, but I haven't tested it.

when running it, you should see something similar to:

```
$ cd (this repository)/scripts
$ sync-to-sd.sh ../examples/sw-led-interrupts/
Mounted /dev/sdb1 at /media/nymphii/04E0-3F26.
sending incremental file list
./
main.py

sent 434 bytes  received 38 bytes  944.00 bytes/sec
total size is 551  speedup is 1.17

/media/nymphii/04E0-3F26 ~/prj/howto-micropython/examples
===== SD Card ======
.
./main.py

~/prj/howto-micropython/examples
Unmounted /dev/sdb1.
```

Using this you can switch between projects in a matter of seconds.

It's very handy while presenting this to a group of people that show
varied interests.
