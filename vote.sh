#!/bin/sh

CWD=$(cd $(dirname "$0") && pwd)

set -o noglob

NUM=$1
AGR="$@"

while getopts ":-:" opt; do
  case $opt in
    -)
          echo "Usage: ./vote.sh VAL|\"None\" [[-i|--input-file FILE]|LIST...]"
          exit 0
;;
    \?)
          echo "Usage: ./vote.sh VAL|\"None\" [[-i|--input-file FILE]|LIST...]"
          exit 0
      ;;  
  esac
done

shift 1;

while getopts ":-:i:" opt; do

  case $opt in
    i)
      if [[ $1 == "-i" ]]; then
      
        if [ -z "$2" ]; then
          echo "File not provided"
          exit 2
        elif [ ! -f "$2" ]; then
          echo "File does not exist: $2"
          exit 2
        fi
        file=$2
        shift 2
        /usr/bin/python3 $CWD/vote.py "$NUM" $(<"$file") "$@"
        exit 0
        
      else 
      echo "Usage: ./vote.sh VAL|\"None\" [[-i|--input-file FILE]|LIST...]"; exit 0 
      fi
      ;;
    -)
      case $OPTARG in
        input-file)
          val="${!OPTIND}"; OPTIND=$(( $OPTIND + 1 ))
          if [ -z "$val" ]; then 
            echo "File not provided"
            exit 1 
          elif [ ! -f "$val" ]; then
            echo "File does not exist: $val"
            exit 2
          fi
          shift 2
          /usr/bin/python3 $CWD/vote.py "$NUM" $(<"$val") "$@"
          exit 0
      ;;
        *)
          echo "Usage: ./vote.sh VAL|\"None\" [[-i|--input-file FILE]|LIST...]"
          exit 0
      ;;
      esac;;
    \?)
          echo "Usage: ./vote.sh VAL|\"None\" [[-i|--input-file FILE]|LIST...]"
          exit 0
      ;;
    :)
      echo "File not provided"
      exit 1
  esac
done

/usr/bin/python3 $CWD/vote.py $AGR
