from lsos_utils import Propeties
import urllib.request
import urllib.parse
import http.cookiejar
import _thread
import pickle
import os
import time

class LsosAutoRun():
	"""docstring for LsosAutoRun"""
	__loginUrl = ''
	__doAutoUrl = ''
	__threadCount = 1
	__loginCookieFile = r'C:/Users/Admin/lsosLongin.txt'
	__loginOpen = {}

	def __getProperties(self):
		p = Propeties("init.properties")
		pro = p.readFile()
		self.__loginUrl = pro['login_url']
		self.__doAutoUrl = pro['do_url']
		self.__threadCount = pro['thread_count']
		pass

	def getThreadCount(self):
		return self.__threadCount
		pass
	def getLoginObj(self):
		return self.__loginOpen
		pass		

	def getLoginUrl(self):
		return self.__loginUrl
		pass

	def getDoAutoUrl(self):
		return self.__doAutoUrl
		pass	

	def loginOpen(self):
		if os.path.exists(self.__loginCookieFile):
			try:
				f = open(self.__loginCookieFile,'rb+')
				print('read login information from lsosLongin.txt')
				self.__loginOpen =  pickle.load(f)
				pass
			except Exception:
				print('open file lsosLongin.txt error')
			finally:
				f.close()
		else:			
			self.__loginOpen = self.login()
		pass

	def login(self,isSave = True):

		#构建cook
		cook=http.cookiejar.CookieJar()
		#构建openner
		openner=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cook))
		#添加headers
		openner.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]
		r=openner.open(self.__loginUrl)
		
		if isSave:
			#持久化
			try:
				f = open(self.__loginCookieFile,'wb+')
				pickle.dump(openner,f)	
				pass
			except Exception:
				print('open file lsosLongin.txt error')
			finally:
				f.close()
			
		print('url: '+self.__loginUrl.split('?',1)[0]+'  ===>  return code :'+ str(r.code))

		self.__loginOpen = self.login()
		pass

	# def doAuto(self):
	# 	openner = self.login()
	# 	r=openner.open(self.__doAutoUrl)
	# 	pass

	# def doAuto(self,threadName,openner):
	# 	print(threadName)
	# 	r=openner.open('http://localhost:8080/lsos/global/catellaeDispatch.do?method=doDispatchExportAddress&id=&queryInter*dcCode=&queryInter*transDateFrom=Tue+Aug+16+00%3A00%3A00+CST+2016&queryInter*transDateTo=Mon+Aug+22+00%3A00%3A00+CST+2016&enterWmsDailyLedgerList_currentPage=1&enterWmsDailyLedgerList_orderBy=&enterWmsDailyLedgerList_paging=true&enterWmsDailyLedgerList_pageSize=10&enterWmsDailyLedgerList_recordCount=2&enterWmsDailyLedgerList_pagingType=0&enterWmsDailyLedgerList_inputColumnsName=enterWmsSMDHeadList*id&addressOids=&queryAddress*addressNumber=&queryAddress*addressName=&queryAddress*latestExportStatus=&queryAddress*supplierId=&queryAddress*customerId=&queryAddress*dcId=&exportAddressDataList_currentPage=1&exportAddressDataList_orderBy=&exportAddressDataList_paging=true&exportAddressDataList_pageSize=10&exportAddressDataList_recordCount=879&exportAddressDataList_pagingType=0&exportAddressDataList_inputColumnsName=&addressNumber=&jspPath=%2Fjsp%2Fglobalarchives%2Fcatellae%2Faddress%2Fcatellae_export_address_list.jsp&nodeId=2c923c6b5437a19f015437a36c600004')
		
	# 	pass

	def __init__(self):
		self.__getProperties()
		self.loginOpen()
		super(LsosAutoRun, self).__init__()
		

	# if __name__ == '__main__':
	# 	getProperties(self)
	# 	doAuto(self)	
def runThead(threadName,openner,runUrl):
	r=openner.open(runUrl)
	print('url: '+runUrl.split('?',1)[0]+'  ===>  return code :'+ str(r.code))
	pass

def doAutoThead():
	a = LsosAutoRun()
	openner = a.getLoginObj()
	for x in range(0,int(a.getThreadCount())):
		try:
			_thread.start_new_thread( runThead, ('thread1',openner,a.getDoAutoUrl(),  ) )
		except Exception:
			print("Error :  无法启动线程")
		pass
	pass
if __name__ == '__main__':
	print('------------------begain do anto-------------------')
	doAutoThead()
	while 1:
		pass
	# a = LsosAutoRun()
	# a.getProperties()
	# a.doAuto()
	print('------------------do auto success-------------------')
	