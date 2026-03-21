from machine import Pin, ADC
import time

led = Pin(4, Pin.OUT)
touch = ADC(26)

THRESHOLD = 5000   # adjust if needed

while True:

    value = touch.read_u16()
    if value < THRESHOLD:
        print("Touch detected!")
        led.value(1)
        time.sleep(2)
        led.value(0)

    time.sleep(0.1)