import os.path
import time
import relay

gpio_to_other_machine_reset = 27
now = time.time()
if os.path.exists("/home/pi/resurrector/last_heartbeat.txt"):
    with open('last_heartbeat.txt', 'r') as f:
        time_of_last_heartbeat = f.readline()
else:
    with open("last_heartbeat.txt", "w") as text_file:
        text_file.write("%s" % now)
print ( now - float(time_of_last_heartbeat) )/60
if now - float(time_of_last_heartbeat) > 5 * 60:
    relay.activate(gpio_to_other_machine_reset)
