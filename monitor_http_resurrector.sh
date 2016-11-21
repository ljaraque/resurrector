#!/bin/bash

until /usr/bin/python /home/pi/resurrector/http_server.py 0.0.0.0; do 
    #echo " Server crashed with coe $?. Respawning..">&2
    sleep 1
done
