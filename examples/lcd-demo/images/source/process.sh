#!/usr/bin/env bash

for filename in *.jpg ; do
    echo ${filename}
    jpegtran ${filename} > ../${filename}
done
