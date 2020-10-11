#### Resurrector Documentation  

### 1. Overview  
`resurrector` package allows to have a machine (At this point a Raspberry Pi) supervising another one.  

An http_server runs in the background receiving keep alive messages from another machine and stores in `last_heartbeat.txt` the UNIX time of the heartbeat received from the other machine through GET to port 80.    

A CRONED watcher (`resurrector.py`) is checking every x minutes if last_heartbeat.txt is older than certain time period.  If so, then it resets the other machine by hardware using GPIO 27.  

### 2. Setup  

Two actions needs to be CRONED:  
- curl <ip_address_of_other_machine>   
- `resurrector.py`  

On the other hand, `http_server.py' must be monitored in order to ensure that it is always up and running.  


