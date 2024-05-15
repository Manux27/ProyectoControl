from time import sleep, perf_counter_ns
from datetime import datetime
import math
import signal
from gpiozero import DigitalInputDevice, DigitalOutputDevice, PWMOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory

in1 = 5
in2 = 6
en = 12

my_factory = PiGPIOFactory()  #hardware pwm supported
motorPWM = PWMOutputDevice(12, pin_factory=my_factory)
motorDIR1 = DigitalOutputDevice(5)
motorDIR2 = DigitalOutputDevice(6)
motorPWM.frequency = 100
motorPWM.value = 0
motorDIR1.value = 0
motorDIR2.value = 0

# for i in range(0,101):
#     
#     motorPWM.value = i*0.01
#     print(i)
#     sleep(0.5)

sleep(60)

print("Acabado, limpiando...")
motorPWM.value = 0
