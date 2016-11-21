#!/bin/bash

until /usr/bin/python /home/pi/rfid_standalone/ugen/ugen.py 0.0.0.0; do 
    #echo " Server crashed with coe $?. Respawning..">&2
    sleep 1
done
