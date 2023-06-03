from microbit import *
from ultrasonic import Ultrasonic
ultrasonic_sensor= Ultrasonic()
while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    if distance_value <16:
        display.scroll(str(int(distance_value)))
        sleep(2000)
        display.scroll("Danger")
    elif distance_value > 15:
        display.scroll(str(int(distance_value)))
        sleep(2000)
        display.scroll("Q")
        