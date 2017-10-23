# Taking Screenshots

With this project loaded onto an

in a pyboard REPL:

```python
>>> import lcd160cr
>>> isinstance(lcd, lcd160cr.LCD160CR)  # assuming lcd already exists
... True
>>> from utils import screenshot
>>> screenshot(lcd, '/sd/screenshot.raw')  # saves .raw file to sd card
```

Copy `screenshot.raw` from the SD Card into this folder.

In this folder...

```bash
$ ./convert.py
screenshot.raw > screenshot.png
```

Now `screenshot.png` should exist in this folder
