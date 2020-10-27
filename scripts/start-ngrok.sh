#!/bin/bash

if [ "$OSTYPE" == "msys" ]; then
  NGROK="winpty ngrok"
else
  NGROK="ngrok"
fi

$NGROK http 12000 --log=stdout
