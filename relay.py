import RPi.GPIO as GPIO
import time


def activate(port):
    try:
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port,0)
        time.sleep(0.15)
        GPIO.output(port,1)
        GPIO.cleanup()
    except:
        GPIO.cleanup()

def main():
    pass

if __name__ == '__main__':
        main()
