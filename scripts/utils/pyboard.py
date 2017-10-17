#!/usr/bin/env python
import serial.tools.list_ports_posix


def comports_with(**kwargs):
    """
    List of serial comports that match the given criteria
    :return: generator of comports connected to arduino
    """
    comports = []
    for c in serial.tools.list_ports_posix.comports():
        if all(getattr(c, k) == v for (k, v) in kwargs.items()):
            comports.append(c)
    return comports


# --- Exceptions
class UniquePyboardError(Exception):
    """Raised when there's an error locating a unique pyboard"""


class PyboardNotFoundError(UniquePyboardError):
    """Raised if the requested board could not be found"""


class MultiplePyboardssFoundError(UniquePyboardError):
    """Raised if multiple connected boards are found with the same serial number"""


# --- Exceptions
class PyboardDevice(object):
    manufacturer = 'MicroPython'

    def __init__(self, serial_number):
        self.serial_number = serial_number
        self._comport = None

    @property
    def comport(self):
        if self._comport is None:
            # --- All serial ports
            ports = comports_with(
                manufacturer=self.manufacturer,
                serial_number=self.serial_number,
            )

            if not ports:
                raise PyboardNotFoundError("no device found with serial_number: '%s'" % self.serial_number)
            elif len(ports) > 1:
                raise MultiplePyboardssFoundError("multiple devices found with serial_number: '%s'" % self.serial_number)
            self._comport = ports.pop()

        return self._comport



# ========================= Mainline =========================
if __name__ == "__main__":
    import argparse

    # ----- Input Parameters
    # Parser
    parser = argparse.ArgumentParser(description="Find Pyboard's COM Port")
    parser.add_argument(
        '--serialnum', '-s', dest='serialnum', default=None, type=str,
        help="Pyboard's serial number (run with --list to list all connected devices)",
    )
    parser.add_argument(
        '--list', '-l', dest='list', default=False, action='store_true',
        help="list all available pyboard serial numbers"
    )

    args = parser.parse_args()


    # ----- Mainline
    if args.list:
        print("Connected Pyboard Serial Numbers:")
        comports = comports_with(manufacturer=PyboardDevice.manufacturer)
        if comports:
            for comport in comports:
                print("    %s : %s" % (
                    comport.serial_number, comport.device,
                ))
        else:
            print("    (none found)")
        exit(0)

    if args.serialnum is None:
        parser.print_help()
        exit(0)


    # print device file to stdout
    print(PyboardDevice(args.serialnum).comport.device)
