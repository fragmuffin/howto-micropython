#!/usr/bin/env bash

# Copy an example onto the pyboard's SD card.
#   - loads pyboard's serial from config
#   - Locates and mounts the pyboard's media
#       - will stop if volume is < 20MB (ie: only an SD card)
#   - sync given folder to sd card
#
# Example Usage:
#   $ sync-to-sd.sh ../examples/sw-led-interrupts


# Defaults
config_file=~/.pyboard-conf.json

# Parameter(s)
source_dir=$1


# Get pyboard device info
serialnum=$(cat ${config_file} | jq -r '.serial_number')
device=$(ls /dev/disk/by-id/usb-uPy_microSD_SD_card_${serialnum}-*-part1)
if [ -z "${device}" ] ; then
    echo "ERROR: couldn't find device file for pyboard:${serialnum}"
    exit 1
fi
uuid=$(udisksctl info --block-device ${device} | grep IdUUID | sed 's/^.*:\s*//')

# Mount drive
function get_mount_point() {
    udisksctl info --block-device ${device} | grep MountPoints | sed 's/^.*:\s*//'
}

mount_point=$(get_mount_point)
if [ -z "${mount_point}" ] ; then
    udisksctl mount --block-device ${device}
    mount_point=$(get_mount_point)
fi

# Verify: device mounted
if [ ! -d ${mount_point} ] ; then
    echo "ERROR while mounting... bugging out"
    exit 1
fi

# Verify: disk size (kB)
volume_size=$(df --output=avail ${mount_point} | tail -n 1)
if [ $volume_size -lt 20000 ] ; then
    echo "Disk size ${volume_size} too small, is the SD card connected?"
    exit 1
fi


# Verify source folder
if [ -z "${source_dir}" ] || [ ! -d ${source_dir} ] ; then
    echo "ERROR: '${source_dir}' is not a directory"
    exit 1
fi
if [ ! -f "${source_dir}/main.py" ] ; then
    echo "ERROR: '${source_dir}/main.py' does not exist"
    exit 1
fi


# Sync files
rsync -aIvzh --delete "${source_dir}/" "${mount_point}/"

# Echo SD file's content
echo
pushd ${mount_point}
echo ===== SD Card ======
find .
echo
popd

# Unmount Drive
udisksctl unmount --block-device ${device}
