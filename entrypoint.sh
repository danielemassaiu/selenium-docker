#!/bin/bash

service xvfb start > /dev/null
export DISPLAY=:10

python /home/app/docker_app.py "$@"