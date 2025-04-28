#!/bin/bash

redis-server &

sleep 10

FLAG=$(cat /answers/flag.txt)

redis-cli set "flag:random" "$FLAG"

tail -f /dev/null
