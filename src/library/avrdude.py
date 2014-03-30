
#project/
#project/src/
#project/another/
def write_hex_file(path, mcu = "atmega32", port = "usb", protocol="stk500"):
	split_str = path.split("/");
	count_element = len(split_str)
	if(os.path.exists(path + "/main.c") && os.path.exists(path + "/makefile")):
		hexfile = path +"/main.hex"
        command = "avrdude -p " + mcu + " -P " + port + " -c " + protocol + " -U flash:w:" + hexfile
		p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
		output, err = p.communicate()
		return str(err)
	else:
		return 0	

def read_hex_file()
