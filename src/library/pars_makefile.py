import sys

words = ['TARG','SRCS','MCU','F_CPU','CFLAGS','LDFLAGS']
info = {}
def parser_makefile(text):
	for line in text:
		for word in line.split():
			if word in words:
				for x in range(len(line)):
					if line[x] == '=':
						if line[x+1] == ' ':
							info[word] = line[x+2:len(line)]
	return info

def change_makefile(text, data):
	count = 0
	for line in text:
		for word in line.split():
			if word in words and word in data.keys():
				for x in range(len(line)):
					if line[x] == '=':
						if line[x+1] == ' ':
							text[count] = line[0:x+2] + data[word] + '\n'
							
		count = count + 1

	strs = ""
	for x in range(len(text)):
		strs += text[x]
	return strs
	

#makefile = open('make','r')
#lines = makefile.readlines()
#makefile.close()
#print parser_makefile(lines)
#print lines[0]
#infos = {}
#infos['TARG'] = "working"
#infos['SRCS'] = "asdf.c"
#infos['CFLAGS'] = "axaaxaxax"
#print change_makefile(lines,infos)