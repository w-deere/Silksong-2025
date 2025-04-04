import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Pin setup
SENSOR_TRIGGER = 23
ECHO = 24
LED = 18

GPIO.setup(SENSOR_TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

led_on = False

def get_distance():
    # Trigger pulse
    GPIO.output(SENSOR_TRIGGER, True)
    time.sleep(0.00001)  # 10us pulse
    GPIO.output(SENSOR_TRIGGER, False)

    # Wait for echo start
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Wait for echo end
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Duration
    duration = end_time - start_time

    # Calculate distance in inches
    distance = duration * 13503.9  # speed of sound in in/sec
    return distance

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance} in")

        if distance <= 5:
            GPIO.output(LED, True)
            led_on = True
        elif distance > 6:
            GPIO.output(LED, False)
            led_on = False

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
