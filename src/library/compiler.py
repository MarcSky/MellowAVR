import sys
import os
import subprocess

def build_project(path):
	print "new path: " + path
	p = subprocess.Popen("cd ~ && cd " +path+ " && make", stdout=subprocess.PIPE, shell=True)
	output, err = p.communicate()
	print "error : " + str(err)
	check_file = os.path.isfile(path+'main.hex')
	return output, check_file

def build_clean(path):
	p = subprocess.Popen("cd ~ && cd " +path+ " && make clean", stdout=subprocess.PIPE, shell=True)
	output, err = p.communicate()
	print "error : " + str(err)
	check_file = os.path.isfile(path+'main.hex')
	return output, check_file

def build_version_gcc():
	p = subprocess.Popen("avr-gcc --version", stdout=subprocess.PIPE, shell=True)
	output, err = p.communicate()
	return output

def build_disasm(path):
	p = subprocess.Popen("cd ~ && cd " +path+ " && avr-objdump -dS main.elf > main.asm", stdout=subprocess.PIPE, shell=True)
	output, err = p.communicate()
	print "error : " + str(err)
	check_file = os.path.isfile(path+'main.asm')
	return output, check_file
	

