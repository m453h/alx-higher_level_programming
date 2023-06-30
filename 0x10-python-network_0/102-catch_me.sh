#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me
curl -o /dev/null -w "You got me!" -sL -X PUT 0.0.0.0:5000/catch_me
