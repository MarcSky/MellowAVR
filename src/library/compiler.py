import sys
import os
import subprocess

def build_project(path):
	print "new path: " + path
	p = subprocess.Popen("cd ~ && cd " +path+ " && make", stdout=subprocess.PIPE, shell=True)
	output, err = p.communicate()
	print "error : " + str(err)
	return output
	
def build_version_gcc():
	p = subprocess.Popen("avr-gcc --version", stdout=subprocess.PIPE, shell=True)
	output, err = p.communicate()
	return output

def disassembler(self):
	return 0

