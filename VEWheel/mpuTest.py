import time
import mpu6050
#import BlynkLib
import RPi.GPIO as GPIO
#from BlynkTimer import BlynkTimer

#BLYNK_AUTH_TOKEN = "UWMRdYcgUPH_pP8NgY1UKO5eeIlYNrOP"

#blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)
#timer = BlynkTimer()

# sync data for virtual pins


#crear nuevo objeto de libreria
mpu6050 = mpu6050.mpu6050(0x68)

def read_sensor_data():
    # leer acelerometro
    accelerometer_data = mpu6050.get_accel_data()
    
    # leer data del giroscopio
    gyroscope_data = mpu6050.get_gyro_data()
    
    # leer temp
    temperature = mpu6050.get_temp()
    
    return accelerometer_data, gyroscope_data, temperature

#Bucle
while True:
    acel,gyro,temp = read_sensor_data()
    
    print("Acel:", acel)
    print("Gyro:", gyro)
    print("Temp:", temp)
    
    time.sleep(0.1)