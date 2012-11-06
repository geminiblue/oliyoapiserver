'''
Created by auto_sdk on 2012-11-05 16:31:45
'''
from top.api.base import RestApi
class WidgetLoginstatusGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.nick = None

	def getapiname(self):
		return 'taobao.widget.loginstatus.get'
