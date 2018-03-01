import Adafruit_BBIO.PWM as PWM
import time
import sys
servoPin="P9_14"
PWM.start(servoPin, 5, 50)
PWM.set_duty_cycle(servoPin,12)
time.sleep(1)
PWM.set_duty_cycle(servoPin,3)