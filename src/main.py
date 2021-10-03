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
        print(scd30.read_measurement())
        time.sleep(5)
