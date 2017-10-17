I use these scripts to easily connect, and upload scripts to my pyboard

> "why do you need scripts?"

(asked nobody)

I'm glad you asked... nobody

**1) device by serial number**

When plugging in multiple serial devices, such as Arduinos, or multiple
MicroPython boards, it can be difficult to track which serial `tty` device connects
to the board you want.

The scripts in this folder locate the devices by their serial number

**2) short commands**

I don't like typing long commands repeatedly, because who does?

**3) scripts are a form of documentation**

A year from now I'll have no recolection of how to do any of this stuff, but

I'll still remember how to read... I hope


# Configuration

These scripts get your pyboard's serial numbmer from a config file

config file: `~/.pyboard-conf.json`

```json
{
    "serial_number": "378446D64987"
}
```

# Scripts

## `connect.sh`

used on it's own, to connect to a console

```
./connect.sh
```
