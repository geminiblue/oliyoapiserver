#encoding=utf-8
from Config import Config
import sys,time
import traceback
import logging
import Func
class LogInfo():
        @staticmethod
        def traceInfo(info):
                sExceptMsg = ""
                if Config.B_SYS_DEBUG:
                    sExceptMsg += "\r\n**********************Trace %s*********************************\r\n"%(Func.fNow())
                    sExceptMsg += "\r\nTrace Messages:%s"%(str(info))
                    sExceptMsg += "\r\n"
                if Config.B_SYS_WRITE_LOG:
                    logger = LogInfo.initlog()
                    logger.info(info)            
                if Config.B_SYS_TRACE:
                        print "\r\nTrace stack is flow:\r\n"
                        traceback.print_stack()
                        print "\r\n"
                if Config.B_SYS_DEBUG:
                        sExceptMsg += "\r\n*********************Trace END**********************************\r\n"
                        print   sExceptMsg                                                  
        @staticmethod
        def writeLog(logLevel,logMessage):
#                alogLevel = ["trace","warning","error"]
                sExceptMsg = ""
                if Config.B_SYS_DEBUG:
                    sExceptMsg += "\r\n**********************%s %s*********************************\r\n"%(logLevel.upper(),Func.fNow())
                    sExceptMsg += "\r\n%s Messages:%s"%(logLevel.upper(),str(logMessage))
                    sExceptMsg += "\r\n"
                if logLevel=="trace":
                        if Config.B_SYS_WRITE_LOG:
                                logger = LogInfo.initlog()
                                logger.info(logMessage)
                        if Config.B_SYS_TRACE:
                                print "\r\nTrace stack is flow:\r\n"
                                traceback.print_stack()
                                print "\r\n"                
                elif logLevel=="warning":
                        pass
                elif logLevel=="error":
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        if exc_type!=None:
                                sExceptMsg += "\r\n"
                                sExceptMsg += repr(traceback.format_tb(exc_traceback))
                                sExceptMsg += "\r\n"
                        else:
                                print "\r\nTrace stack is flow:\r\n"
                                traceback.print_stack()
                                sExceptMsg += "\r\n"
                         
                        if Config.B_SYS_WRITE_LOG and exc_type!=None:
                                logger = LogInfo.initlog()
                                logger.error(sExceptMsg)
                if Config.B_SYS_DEBUG:
                    sExceptMsg += "\r\n*********************%s END**********************************\r\n"%(logLevel.upper())
                    print   sExceptMsg      
        @staticmethod
        def initlog():
                logger = logging.getLogger()
                hdlr = logging.FileHandler(Config.LOG_FILE_NAME%(time.strftime("%Y%m%d",time.gmtime())))
                formatter = logging.Formatter('%(asctime)s %(processName)s %(levelname)s %(message)s')
                hdlr.setFormatter(formatter)
                logger.addHandler(hdlr)
                logger.setLevel(logging.NOTSET)
                return logger
if __name__=="__main__":
    pass
#        try:
#            a=b
#        except Exception,ex:
#            LogInfo.writeLog("error",ex)
