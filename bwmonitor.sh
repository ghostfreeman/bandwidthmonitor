#!/usr/bin/env bash

username=$1
password=$2

if [ -n $username ]; then
  if [ -n $password ]; then
    source ./venv/bin/activate
    python bwmoni.py $username $password
  else
    echo "Invalid arguments, check README.md"
  fi
else
  echo "Invalid arguments, check README.md"
fi
