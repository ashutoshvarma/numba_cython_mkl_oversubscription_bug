#!/usr/bin/env bash

# open fd 3
exec 3<>  /tmp/fd_3

"$@" 1>&3 2>&3 &
pid=$!
trap "kill $pid; echo Exited 1>&3 2>&3" SIGINT SIGTERM

watch -n 0.1 ps -o thcount $pid

