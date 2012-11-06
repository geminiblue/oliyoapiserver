'''
Created by auto_sdk on 2012-11-05 16:31:45
'''
from top.api.base import RestApi
class TaobaokeListurlGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.nick = None
		self.outer_code = None
		self.pid = None
		self.q = None

	def getapiname(self):
		return 'taobao.taobaoke.listurl.get'
