import serial,time,thread
from threading import Timer

pin = ""

class GPRSModule :
	def __init__(self,serial):
		self.serial = serial
		print serial.isOpen()
		self.waitingReply = False

	def write(self,plainCommand):
		self.waitingReply = True
		self.serial.write(plainCommand)
	
	def command(self,command):
		self.write(command + '\r\n')
	
	def AT(self,atCommand):
		self.command('AT+'+ atCommand)
	
	def commandBlocking(self,command):
		self.command(command);
		toRet = []
		while self.waitingReply :
			line = self.readline();
			if line == "" or line == None :
				continue

			toRet.append(line)
#			time.sleep(0.1)
		return toRet

	def ATBlocking(self,atCommand):
		return self.commandBlocking('AT+'+atCommand)	

	def readline(self):
		while self.serial.inWaiting() > 0 :
			line = self.serial.readline().translate(None,'\r\n')
			if line == "OK" or "ERROR" in line :
				self.waitingReply = False
			return line
	
	def doIntro(self):
		print self.ATBlocking("GMI")
		print self.ATBlocking("GMM")
		print self.ATBlocking("GMR")
		print self.ATBlocking("GSN")
		
	
