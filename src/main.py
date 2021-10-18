import time
from machine import I2C, Pin
from scd30 import SCD30

i2cbus = I2C(0, I2C.MASTER, baudrate=20000)
scd30 = SCD30(i2cbus, 0x61)

while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    print("Waiting for sensor to be ready...")
    while scd30.get_status_ready() != 1:
        time.sleep_ms(200)
    print("Sensor ready! Reading measurements")
    while True:
        measurements = scd30.read_measurement()
        # pybytes.send_signal(0, measurements[0])
        # pybytes.send_signal(2, round(measurements[0]))
        # This is stupid.... converting float to int and then to a string
        # is the smallest possible package,
        pybytes.send_signal(3, str(round(measurements[0])))

        print("CO2 (float) - " + str(measurements[0]))
        print("CO2 (int) - " + str(round(measurements[0])))
        # print("Temp - " + str(measurements[1]))
        # print("RH - " + str(measurements[2]))
        time.sleep(5)
