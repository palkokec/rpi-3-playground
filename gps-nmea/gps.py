import serial
import GPSParser

port="/dev/ttyS0"
#    port="/dev/ttyAMA0"
ser=serial.Serial(port, baudrate=9600, timeout=0.5)
gpsParser = GPSParser.GPSParser ()

while True:
    gpsParser.parse (ser.readline())
    print (gpsParser)
