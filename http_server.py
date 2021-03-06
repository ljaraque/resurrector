import time
import BaseHTTPServer
import os.path

HOST_NAME = '0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 80 # Maybe set this to 9000.
PATH = "/home/pi/resurrector/"

#initialize heartbeat to avoid reset on boot due to old heartbeat saved
with open(PATH+"last_heartbeat.txt", "w") as text_file:
    text_file.write("%s" % time.time())

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        time_of_this_heartbeat = time.time()
        #saves current time of current received heartbeat
        with open(PATH+"last_heartbeat.txt", "w") as text_file:
            text_file.write("%s" % time_of_this_heartbeat)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
