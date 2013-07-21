import serial,time,thread
from threading import Timer
from gprsmodule import GPRSModule
from gpsmodule import GPSModule

ser = serial.Serial('/dev/ttyUSB0',9600 ,timeout=2);
ser.open()

ser2 = serial.Serial('/dev/ttyUSB1',115200,timeout=2);
ser2.open()

print ser.isOpen()
print ser2.isOpen()

gps = GPSModule(ser)
gps.run()
gps.runReader()

gsm = GPRSModule(ser2)
gsm.doIntro()
print gsm.ATBlocking("CMEE=2")
