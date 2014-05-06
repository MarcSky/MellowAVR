import serial
import time
ser = 0

def open_connect(s_port, s_baudrate):
	ser = serial.Serial(
		port=s_port,
		baudrate=s_baudrate,
		parity=serial.PARITY_ODD,
		stopbits=serial.STOPBITS_TWO,
		bytesize=serial.SEVENBITS
	)

	ser.open()

def close_connect():
	ser.close()
	
def send_char(char):
	ser.write(char)
	
def read_char():
	if ser.isOpen():
		try:
			time.sleep(1)
			while ser.inWaiting()>0:
				return ser.read(1)
		except serial.SerialException:
			continue
