import time
from machine import I2C, Pin, ADC
from scd30 import SCD30

# The number of milliseconds from the initial boot until a crash occurs
# where we want it to restart gracefully. This is to prevent a panic where
# the device gets stuck in a loop during boot for some reason, but in a normal
# error case we want a restart to happen
RESTART_GRACE_PERIOD = 10000

pybytes.send_signal(5, "BOOTING")

# Get the starting tick value
start = time.ticks_ms()
print("Start", start, "ms")

# We pull the battery level to be able to track it over time
adc = ADC()
bat_voltage = adc.channel(attn=ADC.ATTN_11DB, pin='P16')

# Setup the I2C bus and set a baudrate supported by the sensors
i2cbus = I2C(0, I2C.MASTER, baudrate=20000)

# Setup the library used to communicate and decode the data from the sensor
# This uses the address specified for the sensor.
scd30 = SCD30(i2cbus, 0x61)


# Wrap everything in try catch to be able to recover from any and all errors
# as long as it's been longer than the RESTART_GRACE_PERIOD
try:
    print("Waiting for the sensor to warm up")

    vbat = bat_voltage.voltage()
    pybytes.send_signal(4, str(vbat*2))

    pybytes.send_signal(5, "WARMING_UP")
    # Wait 5 minutes initially to allow the sensor to warm up
    iterator = 0
    while iterator < 10:
        vbat = bat_voltage.voltage()
        pybytes.send_signal(4, str(vbat*2))
        iterator = iterator + 1
        time.sleep(30)

    pybytes.send_signal(5, "WARM")

    # Set the measurement interval to 60 seconds
    scd30.set_measurement_interval(60)

    # The temperature readings are affected by heatup from the pcb
    # I've found it to be around 2 degrees, so we offset it by that amount
    scd30.set_temperature_offset(2)
    while True:
        print("Sensor ready! Reading measurements")
        pybytes.send_signal(5, "READY")
        while True:
            pybytes.send_signal(5, "MEASURE")

            # Wait for sensor data to be ready to read (by default every 2 seconds)
            print("Waiting for sensor to be ready...")
            while scd30.get_status_ready() != 1:
                time.sleep_ms(200)

            measurements = scd30.read_measurement()
            # This is stupid.... converting float to int and then to a string
            # is the smallest possible package
            pybytes.send_signal(1, str(round(measurements[1])))
            pybytes.send_signal(2, str(round(measurements[2])))
            pybytes.send_signal(3, str(round(measurements[0])))
            print("Sent new measurement - " + str(round(measurements[0])))

            # Send an update on the battery level
            vbat = bat_voltage.voltage()
            pybytes.send_signal(4, str(vbat*2))

            # time.sleep(5)
            time.sleep(60 * 1)
except Exception as e:
    # Todo: Handle exception, write to file?
    if time.ticks_ms() - start > RESTART_GRACE_PERIOD:
        import machine
        machine.reset()
    else:
        print("Error occurred to quickly to gracefully restart")
        import sys
        sys.print_exception(e)
        pycom.rgbled(0xFF0000)
        time.sleep(60*60)
