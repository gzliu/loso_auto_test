import pickle
import os
import time
import codecs
import re

class Propeties():
	"""docstring for Propeties"""
	filePath = ""

	def readFile(self):
		properties = {}
		__index = 0
		__code = ''
		# f = open(self.filePath,'r')
		# for line in f:
		# 	if line.find("=") > 0:
		# 		strs = line.replace("/n","").split("=")
		# 		properties[strs[0]] = strs[1]
		try:
			f = open(self.filePath,'rb')
			txt = f.read()
			f.close()

			if txt[:3] == codecs.BOM_UTF8:
				txt = txt[3:].encode('utf-8')
				pass
				
			if type(txt) == bytes:
				txt = '%s'%(txt)
				pass

			for line in txt.split('\r\n'):
				if re.match(r'^#.*',line,re.U):
					continue
					pass
				if line.find("=") > 0:
					paramters = line.split("=",1)
					properties[paramters[0]] = properties[paramters[1]]
					pass
				pass				
		except Exception as e:
			raise e
		else:
			f.close()
		finally:
			f.close()
		return properties
		
	def __init__(self, filePath):
		super(Propeties, self).__init__()
		self.filePath = filePath

	#if __name__ == '__main__':
	#		readFile()	

# p = Propeties("init.properties")		
# d = p.readFile()	
# print(d['login_url'])
# print(d['do_url'])

testDict = {'name':'ming',"age":12}		
testFile = open('pickle.txt','wb+')

pickle.dump(testDict,testFile)
stinfo = os.stat('pickle.txt')
print ("a2.py 的访问时间: %s" %stinfo.st_atime)
print ("a2.py 的修改时间: %s" %stinfo.st_mtime)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stinfo.st_atime)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stinfo.st_mtime)))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

f = open('init.properties','rb')
index = 0
code = ''
txt = f.read()
f.close()

print(type('txt'))
if txt[:3] == codecs.BOM_UTF8 :
	txt = txt[3:].decode('utf-8')

# for line in txt.split('\r\n'):
# 	if not re.match(r'^#.*',line,re.U) :

# 		print(line)
# 	pass
# for line in f:
# 	if index == 0 and line[:3] == codecs.BOM_UTF8:
# 		code = 'utf-8'
# 		s = "%s" % (line[3:])
# 		lines =s.encode('utf-8')
# 		print(lines)
# 		pass
# 	if code == 'utf-8':
# 		s = "%s" % (line)
# 		lines = s.encode('utf-8')
# 	#print(lines)
# 	#print(re.search(r'(?#...)', "%s" % (line)))
# 	pass

# by = f.read()
# f.close()

# print(by[3:].decode('utf-8'))
      
# if os.path.exists('pickle.txt'):
# 	f = open('pickle.txt','rb+')
# 	datas = pickle.load(f)
# 	f.close()
# 	print(datas['name'])
# else:			
# 	print('can not find file')
# pass