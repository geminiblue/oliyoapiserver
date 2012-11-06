#encoding=utf8
'''
Created on 2012-9-24

@author: Administrator
'''

class Singleton(object):   
    def __new__(cls): 
        import threading   
        mylock = threading.RLock()   
        mylock.acquire()   
        cls.instance = object.__new__(cls)   
        cls.__new__ = cls.Instance   
        cls.instance.init()
        mylock.release()
        return cls.instance
    @classmethod   
    def Instance(cls, type):   
        return cls.instance   
    def init(self):   
        pass