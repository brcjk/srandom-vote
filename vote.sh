#!/bin/bash

CWD=$(pwd)





while getopts ":-:" opt; do
  case $opt in
    -)
      echo "Usage: ./vote.sh VAL [LIST]"
      exit 0
      ;;
  esac
done

/usr/bin/python3 $CWD/vote.py "$@"