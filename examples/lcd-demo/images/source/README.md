# Source Images

These are the original images to display on the LCD.

## Require Post-processing

They're not accessed from here, because they require post-processing
on a computer before they can be displayed by the LCD's drivers.

read more here:
https://forum.micropython.org/viewtopic.php?f=6&t=3074&p=18147#p18147

## Post process script

`process.sh`

This script processes all `*.jpg` files in this folder into the `..` folder.

requires `jpegtran`, installed on ubuntu with

```
sudo apt install libjpeg-progs
```
