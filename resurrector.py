import os.path
from os import system
import time
import relay

PATH = "/home/pi/resurrector/"
GATEWAY = "10.1.1.100"

gpio_to_other_machine_reset = 27
now = time.time()
if os.path.exists(PATH + "last_heartbeat.txt"):
    with open(PATH + 'last_heartbeat.txt', 'r') as f:
        time_of_last_heartbeat = f.readline()
else:
    with open(PATH + "last_heartbeat.txt", "w") as text_file:
        text_file.write("%s" % now)
print ( now - float(time_of_last_heartbeat) )/60
if now - float(time_of_last_heartbeat) > 5 * 60 and system("ping -c 1 " + GATEWAY) == 0: #check alive but if network is up
    relay.activate(gpio_to_other_machine_reset)
