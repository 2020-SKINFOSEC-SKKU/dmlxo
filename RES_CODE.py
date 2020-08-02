#!/bin/bash
RES_CODE=$(curl -o /dev/null -w "%{http_code}" "http://115.145.212.130:8080")

if [ $STATUS -eq 200 ]; then
  echo "OKOK"
fi
