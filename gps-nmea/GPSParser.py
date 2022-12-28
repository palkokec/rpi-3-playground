import serial
import time
import string
import pynmea2
from pprint import pprint


class GPSParser:
    gga = {} #Global Positioning System Fixed Data
    gll = {} #Geographic Position-- Latitude and Longitude
    gsa = {} #  GNSS DOP and active satellites
    gsv = {} #$Talker ID+GSV  GNSS satellites in view
    rmc = {} #$Talker ID+RMC  Recommended minimum specific GPS data
    vtg = {} #$Talker ID+VTG  Course over ground and ground speed
    other = {}

    def __init__(self):
        pynmea2.NMEAStreamReader()

    def __str__(self):
        pprint (self.gga)
        pprint (self.gll)
        pprint (self.gsa)
        pprint (self.gsv)
        pprint (self.rmc)
        pprint (self.vtg)
        pprint (self.other)

        return f"""Global Positioning System Fixed Data: {self.gga}
        Geographic Position-- Latitude and Longitude: {self.gll}
        GNSS DOP and active satellites: {self.gsa}
        GNSS satellites in view: {self.gsv}
        Recommended minimum specific GPS data: {self.rmc}
        Course over ground and ground speed: {self.vtg}
        Other {self.other}
    """

    def parse(self,data):
        try:
            if ("GGA" in data.decode("utf-8")):
                self.gga = pynmea2.parse(data.decode("utf-8"))
            elif ("GLL" in data.decode("utf-8")):
                self.gll = pynmea2.parse(data.decode("utf-8"))
            elif ("GSA" in data.decode("utf-8")):
                self.gsa = pynmea2.parse(data.decode("utf-8"))
            elif ("GSV" in data.decode("utf-8")):
                self.gsv = pynmea2.parse(data.decode("utf-8"))
            elif ("RMC" in data.decode("utf-8")):
                self.rmc = pynmea2.parse(data.decode("utf-8"))
            elif ("VTG" in data.decode("utf-8")):
                self.vtg = pynmea2.parse(data.decode("utf-8"))
            else:
                self.other = pynmea2.parse(data.decode("utf-8"))
        except pynmea2.ParseError as e:
            print('Parse error: {}'.format(e))

