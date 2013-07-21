import serial,time,thread
from threading import Timer


class GPSModule:
	def __init__(self,serial):
		self.serial = serial
		self.latitude = ["",""]
		self.longitude = ["",""]

	def parseGPSLine(self,line):
		if line == None or line == "" : 
			return ""
		tokens = line.split(',');
		if tokens[0] == None or tokens[0] == "":
			return ""
		if tokens[0][0] != '$' : 
			return None
		tokens[0] = tokens[0].lstrip('$')
		if tokens[0] == "GPGLL" :
			self.latitude[0]=tokens[1]
			self.latitude[1]=tokens[2]
			self.longitude[0]=tokens[3]
			self.longitude[1]=tokens[4]

	def readFromGPS(self):
		toRet=""
		if self.serial.inWaiting() > 0 :
			toRet = self.serial.readline()
			toRet = toRet.translate(None,'\n\r')
		return toRet
	
	def run(self):
		self.parseGPSLine(self.readFromGPS())
		self.timer = Timer(0.1,self.run)
		self.timer.start()
	
	def runReader(self):
		print self.latitude +  self.longitude
		self.readTimer = Timer(1,self.runReader)
		self.readTimer.start()
	
	def stop(self):
		self.timer.cancel()
	
	def stopReader(self):
		self.readTimer.cancel()
	


