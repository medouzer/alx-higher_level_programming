#!/bin/bash
#cURL only methods

curl -sI "$1" | grep "Allow" | awk '{print $2 " " $3 " " $4}'
