import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set GPIO pin 8 as an output
GPIO.setup(8, GPIO.OUT)

try:
    # Turn on GPIO pin 8
    GPIO.output(8, GPIO.HIGH)
    print("GPIO pin 8 is ON")
    time.sleep(4)  # Wait for 1 second

    # Turn off GPIO pin 8
    GPIO.output(8, GPIO.LOW)
    print("GPIO pin 8 is OFF")
    time.sleep(1)  # Wait for 1 second

finally:
    # Clean up
    GPIO.cleanup()
