#!/usr/bin/python
 
import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([ 6 | (channel&4) >> 2, (channel&3)<<6, 0])
  data = ((adc[1]&15) << 8) + adc[2]
  return data
  
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 5) / float(1023)
  volts = round(volts,places)
  return volts
 
# Function to calculate temperature from
# TMP36 data, rounded to specified
# number of decimal places.
def ConvertTemp(data,places):
 
  # ADC Value
  # (approx)  Temp  Volts
  #    0      -50    0.00
  #   78      -25    0.25
  #  155        0    0.50
  #  233       25    0.75
  #  310       50    1.00
  #  465      100    1.50
  #  775      200    2.50
  # 1023      280    3.30
 
  temp = ((data * 330)/float(1023))-50
  temp = round(temp,places)
  return temp
 
# Define delay between readings
delay = 0.5
 
while True:
    values = [0]*8
    volts = [0]*8
    temps = [0]*8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = (ReadChannel(i))
        temps[i] = (ConvertTemp(values[i],2))
        volts [i] = (ConvertVolts(values[i],2))

    # Print the ADC values.
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*volts))
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*temps))
    time.sleep(delay)
