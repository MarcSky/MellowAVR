import ConfigParser
import os.path
class parser_config():
	def __init__(self):
		self.default_config = 'config'
		self.parser = ConfigParser.ConfigParser()
		self.filepath = ""
	
	def set_path(self,path):
		self.filepath = path
		self.parser.read(self.filepath + '/mellow.mcf')
	
	def get_path(self):
		return self.filepath
	
	def get_param(self,name):
		return self.parser.get(self.default_config, name)
	
	def set_param(self, name, value):
		self.parser.set(self.default_config, name, value)
	
#x = parser_config()
#x.set_path('/home/juster/asdfa')
#print x.get_param('project_name')
#x.set_param('project_name', 'aaaaa')
#print x.get_param('project_name')
#print x.get_path()
#con = "/home/juster/path/main.c"
##x = con.split('/')
##print x
#print len(x)
#print x[1:len(x) - 1]
##print '/'.join(x[1:len(x)-1])
#if os.path.isfile('/home/juster/mellow.cnf'):##
	#print "s"#

#print x[1:len(x) - 2]
#if (len(x) - 4) == 1:#
	#print "ss"


#def find_config(path):
#	dic = path.split('/')
#	size = len(dic)
#	count = 1
#	while (size - count > 1):
#		new_path = '/'.join(dic[1:size - count])
#		count = count + 1
#		a = '/'+new_path+'/'
#		if os.path.isfile(a + 'mellow.cnf'):
#			return a
#	return 0
#
#print find_config('/home/juster/asdfa/src/jhgjhg/main.c')
