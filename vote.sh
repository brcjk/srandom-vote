#!/bin/bash

CWD=$(cd $(dirname $0) && pwd)

NUM=$1
AGR="$@"

while getopts ":-:i:" opt; do
  case $opt in
    i) 
      if [ ! -f "$OPTARG" ]; then
        echo "File does not exist"
        exit 2
      fi
      /usr/bin/python3 $CWD/vote.py "" $(cat $OPTARG); exit 0;;
    
    -)
      case $OPTARG in
        *)
          echo "Usage: ./vote.sh [VAL] [-i|--input-file FILE]|LIST]"
          exit 0
      ;;
      esac;;
    \?)
          echo "Usage: ./vote.sh [VAL] [-i|--input-file FILE]|LIST]"
          exit 0
      ;;  
    :)
      echo "File not provided"
      exit 1
      ;;
  esac
done

shift 1;

while getopts ":-:i:" opt; do
  case $opt in
    i)
      if [ ! -f "$OPTARG" ]; then
        echo "File does not exist"
        exit 2
      fi
      /usr/bin/python3 $CWD/vote.py $NUM $(cat $OPTARG)
      
      exit 0
      ;;
    
    -)
      case $OPTARG in
        input-file)
          val="${!OPTIND}"; OPTIND=$(( $OPTIND + 1 ))
          if [ -z "$val" ]; then 
            echo "File not provided"
            exit 1 
          fi
          /usr/bin/python3 $CWD/vote.py $NUM $(cat $val)
          exit 0
      ;;
        *)
          echo "Usage: ./vote.sh [VAL] [-i|--input-file FILE]|LIST]"
          exit 0
      ;;
      esac;;
    \?)
          echo "Usage: ./vote.sh [VAL] [-i|--input-file FILE]|LIST]"
          exit 0
      ;;
    :)
      echo "File not provided"
      exit 1
  esac
done

/usr/bin/python3 $CWD/vote.py $AGR