## IMPORTANT NOTICE: YOU MUST ADD THE BELOW LINE TO THE 'REQUIREMENTS.TXT' FILE AND PROPERLY INSTALL IT
#   adafruit-circuitpython-bme280


# Author: Colby Sawyer 11-18-2021

## NOTICE: this file is intended for the BME280 to be connected via I2C

from typing import Sequence
import board
import time
from adafruit_bme280 import basic as adafruit_bme280

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()   # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

def get_data():
    sensor_data = bytearray(7)
    FEATHER_ID = 1

    temp_val = bme280.temperature
    humid_val = bme280.relative_humidity
    press_val = bme280.pressure

    sensor_data[0] = FEATHER_ID
    # Temperature data
    sensor_data[1] = (temp_val >> 8) & 0xff
    sensor_data[2] = temp_val & 0xff
    # Humidity data
    sensor_data[3] = (humid_val >> 8) & 0xff
    sensor_data[4] = humid_val & 0xff
    #Pressure Data
    sensor_data[5] = (press_val >> 8) & 0xff
    sensor_data[6] = press_val & 0xff
    
    return sensor_data
