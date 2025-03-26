#!/bin/sh

input="./flag.txt"

while read -r line
do
  echo "$line"
done < "$input"

