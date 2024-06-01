import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set GPIO pin 8 as an output
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.HIGH)

from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a GET endpoint
@app.get("/on")
async def read_root():
    # Turn on GPIO pin 4
    GPIO.output(7, GPIO.LOW)
    print("GPIO pin 7 is ON")
    time.sleep(4)  # Wait for 1 second

    # Turn off GPIO pin 4
    GPIO.output(7, GPIO.HIGH)
    print("GPIO pin 7 is OFF")
    time.sleep(1)  # Wait for 1 second

    return {"Hello": "World"}
