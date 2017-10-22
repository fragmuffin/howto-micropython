#!/usr/bin/env bash

# Defaults
config_file=~/.pyboard-conf.json


function config_file_error() {
cat << EndOfMessage
config file $1: ${config_file}
file should be in json format, and would be something like:

{
    "serial_number": "378446D64987"
}
EndOfMessage
}

if [ ! -f ${config_file} ] ; then
    config_file_error "does not exist"
    exit 1
fi

# Get configured serial number
serialnum=$(cat ${config_file} | jq -r '.serial_number')
device=$(utils/pyboard.py -s ${serialnum})

echo "Connecting to pyboard:"
echo "    serial number: ${serialnum}"
echo "    device:        ${device}"
cu -l ${device}
