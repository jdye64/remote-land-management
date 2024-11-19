import RPi.GPIO as GPIO
import time

# Define pin
switchPin = 21

# Pin Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Pin State Setup
prevState = 'Unknown'
state = 'Unknown'

try:
    while 1:
        prevState = state

        if GPIO.input(switchPin): # Switch is released
            state = 'Opened'
        else: # Switch is connected
            state = 'Closed'

        if prevState!=state:
            print(state)
            # Additional function coming to write current state to JSON file for API

        time.sleep(0.1)
except KeyboardInterrupt: # Clean Exit
    GPIO.cleanup() # Cleanup all GPIO

except Exception as e: # Catch Errors
    print(e)
