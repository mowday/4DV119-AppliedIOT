import time
from machine import I2C, Pin
from scd30 import SCD30

# Setup the I2C bus and set a baudrate supported by the sensors
i2cbus = I2C(0, I2C.MASTER, baudrate=20000)

# Setup the library used to communicate and decode the data from the sensor
# This uses the address specified for the sensor.
scd30 = SCD30(i2cbus, 0x61)

print("Waiting for the sensor to warm up")
# Wait 5 minutes initially to allow the sensor to warm up
time.sleep(5 * 60)

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
