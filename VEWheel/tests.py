from time import sleep, perf_counter_ns
#from mpu9250_jmdev.registers import *
#from mpu9250_jmdev.mpu_9250 import MPU9250
import mpu9250_jmdev
import math

imu = MPU9250(bus=1, gfs=GFS_250, afs=AFS_2G)
imu.abias = [0.013221153846153846, -0.030993339342948716, 0.004657451923076872]
imu.gbias = [1.3726094563802083, 1.2428309122721355, 0.00033772786458334]
imu.configure()

startTime = perf_counter_ns()
lastGyroTime = perf_counter_ns()
lastPrintTime = perf_counter_ns()
time = 0
loopCount = 0
gyroAngle = 0
measuredAngle = 0
filteredAngle = 0
Kfiltro = 0.99999

while True:
    # read accel
    ax, ay, az = imu.readAccelerometerMaster()  #[G]
    accAngle = math.atan(-ax / math.sqrt(pow(ay, 2) + pow(az, 2))) * 180 / math.pi  #[deg]
    
    # read gyro
    gx, gy, gz = imu.readGyroscopeMaster() #[deg/s]
    timeDelta = (perf_counter_ns() - lastGyroTime) / 1e9  #[sec]
    lastGyroTime = perf_counter_ns()
    gyroAngleDelta = gz * timeDelta
    if math.isnan(gyroAngle): gyroAngle = accAngle
    gyroAngle += gyroAngleDelta  #[deg]
    
    # filtrar angulo
    if math.isnan(measuredAngle): measuredAngle = accAngle
    measuredAngle = (Kfiltro * (measuredAngle + gyroAngleDelta) +
                     (1-Kfiltro) * accAngle)  #[deg]
    print(f"{measuredAngle} + {gyroAngle} + {accAngle}")
    
    sleep(0.02)
