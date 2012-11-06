#encoding=utf8
'''
Created on 2012-9-18

@author: Administrator
'''

import os
from Config import Config
class Pinyin(object):
    def __init__(self):
        self.dict = {}
        for line in open(Config.S_PINYIN_DB_FILE):
            k, v = line.split('\t')
            self.dict[k] = v

    def get_pinyin(self, chars='', splitter=''):
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                result.append(self.dict[key].split(" ")[0].strip()[:-1].lower())
            except Exception,e:
#                print e;
                result.append(char)
        return splitter.join(result)

    def get_initials(self, char=''):
        try:
            return self.dict["%X" % ord(char)].split(" ")[0][0]
        except:
            return char
if  __name__=="__main__":
    p = Pinyin()
    print p.get_pinyin(u"行你需要")

        