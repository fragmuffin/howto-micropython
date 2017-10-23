# Configuration

These scripts get your pyboard's serial numbmer from a config file

config file: `~/.pyboard-conf.json`

```json
{
    "serial_number": "378446D64987"
}
```

# Scripts

## `repl.sh`

Connects to a REPL on the pyboard with configured serial number

```
./repl.sh
```

## `sync-to-sd.sh`

Flashes a project directory onto the SD card connected to the pyboard with the
configured serial number.

* Finds device
* Mounts SD Card
* Verifies source & destination
* Coppies onto & deletes extra files from mounted SD Card
* unmount SD card

** Usage: **

```
./sync-to-sd.sh ../examples/lcd-demo/
```
