#!/bin/sh

cat /proc/$(ps -ef | grep ${PROCESS_GREP_REGEX} | awk '{print $2}')/fd/1