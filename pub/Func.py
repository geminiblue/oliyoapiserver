#encoding=utf8
'''
Created on 2012-10-12

@author: Administrator
'''
from Config import Config
from Pinyin import Pinyin
from twisted.protocols.basic import LineReceiver
import hashlib
import math
import sys
import time
from LogInfo import LogInfo




def getConfig(keyName):
    return Config.cfg[keyName]

def debugInfo(info):   
    LogInfo.traceInfo(info)

def getNow():
    return  int(time.time())
def md5(sStr):
    '''
    返回字符串的md5加密
    @param sStr:string  要加密的字符串
    @return:string 加密后的字符串
    '''
    if sStr != "":
        return hashlib.md5(sStr).hexdigest()
    else:
        return None
def fNow():
    '''
    返回格式化后的时间
    '''
    return time.strftime("%Y - %m - %d %H:%M:%S", time.gmtime())
def callSysErr(CommandId, ErrorNum):
    return "SYS#%s#%s" % (CommandId, ErrorNum)

    


def sendMsgStr(sockObj,sendStr):
    if not sendStr:
        return ;
    if not sockObj:
        return ;
 
    if(sockObj):        
        if isinstance(sockObj, dict):            
            for sock in sockObj.values():
                if isinstance(sock, LineReceiver):                                        
                    sock.sendLine(sendStr);
        if isinstance(sockObj, tuple) or isinstance(sockObj, list):            
            for sock in sockObj:
                if isinstance(sock, LineReceiver):  
                                                        
                    sock.sendLine(sendStr);
                    
        elif isinstance(sockObj, LineReceiver):                 
            sockObj.sendLine(sendStr);
        else:
            pass;
    



def sendMsg(sockObj, cmd, cmdId=0, Message=[]):
    '''
        发送消息
        @param sockObj:指定的客户端
        @param cmd: 命令
        @param cmdId:命令标识
        @param Message:发送的数据   
    '''
    
    if not Message:
        return ;
    if not sockObj:
        return ;
    
    sendStr = "%s#%s" %(cmd,cmdId);
    for msg in Message:
        sendStr=sendStr+"#"+msg;    
    if(sockObj):        
        if isinstance(sockObj, dict):            
            for sock in sockObj.values():
                if isinstance(sock, LineReceiver):                                        
                    sock.sendLine(sendStr);
        if isinstance(sockObj, tuple) or isinstance(sockObj, list):            
            for sock in sockObj:
                if isinstance(sock, LineReceiver):  
                                                        
                    sock.sendLine(sendStr);
                    
        elif isinstance(sockObj, LineReceiver):                 
            sockObj.sendLine(sendStr);
        else:
            pass;
    
      
    

def sendError(sockObj, cmdId=0, Message=None):
    if(sockObj):        
        if isinstance(sockObj, dict):            
            for sock in sockObj.values():
                if isinstance(sock, LineReceiver):                                        
                    sock.sendLine(Config.SYS_ERROR_COMMAND % (cmdId, Message));
        if isinstance(sockObj, tuple) or isinstance(sockObj, list):            
            for sock in sockObj:
                if isinstance(sock, LineReceiver):  
                                                        
                    sock.sendLine(Config.SYS_ERROR_COMMAND % (cmdId, Message));
                    
        elif isinstance(sockObj, LineReceiver):                 
            sockObj.sendLine(Config.SYS_ERROR_COMMAND % (cmdId, Message));
        else:
            pass;
    

def subString (s, length, isEnd=False):
    s = u"%s" % (s);
    result = "";
    try:
        if isEnd:
            result = s.decode('utf8')[:-length].encode('utf8');
        else:
            result = s.decode('utf8')[:length].encode('utf8');
    except:
        pass;
    return result;



    
def validPinyin(oneWord, twoWord):
    '''
            比对文字拼音
    @param oneWord:第一个字
    @param twoWord:第二个字
    @return: boolean
     
    '''
    oneWord = subString(oneWord, 1);
    twoWord = subString(twoWord, 1);

    if not Config.pinYin:
        pinYin = Pinyin();
    onePinyin = pinYin.get_pinyin(u"%s" % toStr(oneWord));
    twoPinyin = pinYin.get_pinyin(u"%s" % toStr(twoWord));
   
    return onePinyin == twoPinyin;

    
    
        


def toFloat(value,defalutValue=0.0):
    try:
        return float(value);
    except:
        return defalutValue;
            
                
def toInt(value, defalutValue=0):
    try:
        return int(value);
    except:
        return defalutValue;
        

def strToInt(intValue, defalutValue= -1):
    return toInt(intValue, defalutValue);


def intToStr(strValue, defalutValue=""):
    return toStr(strValue, defalutValue);
def toStr(strValue, defalutValue=""):
    try:
        return str(strValue);
    except:
        return defalutValue;
def deg2rad(d): 
    """degree to radian""" 
    return d * math.pi / 180.0
def spherical_distance(frompoint, topoint): 
    """
    经纬度转换为距离 caculate the spherical distance of two points 
    @param frompoint:tuple 开始经纬度(经度,纬度) 
    @param topoint:tuple 结束经纬度(经度,纬度) 
    @return: floor    
    """ 
    flon = deg2rad(frompoint[1])
    flat = deg2rad(frompoint[0])
    tlon = deg2rad(topoint[1]) 
    tlat = deg2rad(topoint[0])
    con = math.sin(flat) * math.sin(tlat)
    con += math.cos(flat) * math.cos(tlat) * math.cos(flon - tlon) 
    return math.acos(con) * Config.EARTH_RADIUS_METER
if __name__ == "__main__":
    
    validPinyin("意她", "衣");
    

