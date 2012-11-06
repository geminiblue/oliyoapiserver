#encoding=utf8
'''
Created on 2012-9-17

@author: Administrator
'''

from DBUtils.PooledDB import PooledDB
from Singleton import Singleton
from mysql.connector import errorcode
from pub import Func
from pub.Config import Config
from pub.LogInfo import LogInfo
import mysql.connector
class DbManager(Singleton):
    '''
    数据库连接池对象
    '''
    def __init__(self):
        self.__pool = PooledDB(mysql.connector,mincached=0, maxcached=10, maxshared=10, maxusage=10000, **Func.getConfig("DbConnectString"))
    def getConnection(self):
        '''
        从连接池中取出的数据连接对象
        '''
        return self.__pool.connection()
    
class DbOperator():
    '''
    '''

    def __init__(self):
        try:
            self.__dbHandle = DbManager().getConnection()
            self.__cursor = self.__dbHandle.cursor()
        except mysql.connector.Error as err:
            self.__dbError(err)
    def __del__(self):
        try:
            self.__cursor.close()
            self.__cursor = None
            self.__dbHandle.close()
            self.__dbHandle = None
        except:
            pass
    def query(self):
        pass
    def findByPK(self,Sql):
        try:
            self.__cursor.execute(Sql)
            return self.__cursor.fetchone()
        except mysql.connector.Error as err:
            self.__dbError(err)
    def getCursor(self):
        return self.__cursor
    def getOne(self,Sql):
        try: 
            self.__cursor.execute(Sql)
            result = self.__cursor.fetchone()
            if(result!=None):
                return dict(zip(self.__cursor.column_names, result))
            else:
                return Config.S_SYS_NONE
        except mysql.connector.Error as err:
            self.__dbError(err)
    def getFieldByCondition(self,aParam):
        '''
        根据条件查询内容
        '''
        resultRow = 1
        if(aParam!=None):

            sSql = " SELECT %s FROM %s WHERE 1=1  AND %s "
            if( aParam.has_key(Config.HAS_JOIN) and  aParam[Config.HAS_JOIN]!=""):
                sSql = " SELECT %s FROM %s " + aParam[Config.HAS_JOIN] +" WHERE 1=1 AND %s"
            condition = " AND 1=1 "
            SearchFields = " * "
            if( aParam.has_key(Config.S_SEARCHFIELDS) and  aParam[Config.S_SEARCHFIELDS]!=""):
                SearchFields=aParam[Config.S_SEARCHFIELDS]
            if(aParam.has_key(Config.S_SEARCHCONDITION) and aParam[Config.S_SEARCHCONDITION]!=""):
                condition=aParam[Config.S_SEARCHCONDITION]
            if(aParam.has_key(Config.S_RESULTROW) and aParam[Config.S_RESULTROW]>1):
                resultRow=aParam[Config.S_RESULTROW]

            sSql = sSql % (SearchFields,aParam[Config.S_TABLE],condition)
#            Func.debugInfo(sSql)
            if(aParam.has_key(Config.S_ORDERBY) and aParam[Config.S_ORDERBY]!=""):
                sOrderBy = aParam[Config.S_ORDERBY]
                sSql = sSql+(" ORDER BY %s" % sOrderBy )
            if(aParam.has_key(Config.S_LIMIT) and aParam[Config.S_LIMIT]!=""):
                sLimit = aParam[Config.S_LIMIT]
            else:
                sLimit = " 1 ";
            if(aParam.has_key(Config.S_FETCH_ALL) and aParam[Config.S_FETCH_ALL]==False):
                    sSql = sSql + (" LIMIT %s"%sLimit)
            Func.debugInfo(sSql)
            if(resultRow>1):
                return self.findAll(sSql)
            else:
                return self.getOne(sSql)
        else:
            return None
    def findAll(self,Sql=None):
        result = None
        try:
            self.__cursor.execute(Sql,)
            tmp = self.__cursor.fetchall()
            result = []
            if(tmp!=None):
                for tt in tmp:
                    result.append(dict(zip(self.__cursor.column_names,tt )))
        except mysql.connector.Error as err:
            self.__dbError(err)        
        return result
    def doExecute(self,sSql):
        '''
                        执行一条sql语句，并返回所影响的行数     
        @aParam 
        '''
        if not sSql:
            return 0;
        try:
            self.__cursor.execute(sSql);
#            print self.__cursor.execute(sSql);
            self.__dbHandle.commit()
            return 1
        except mysql.connector.Error as err:       
            self.__dbError(err)           
            return 0
    
    def executeAndGetId(self,Sql,Param=None):
        '''
        执行Sql语句并返回递增Id
        @param Sql:要执行的Sql语句
        @param Param:Sql语句中所要使用的参数
        @return:int  
        '''
        try:
            if Param == None:  
                self.__cursor.execute(Sql)  
            else:  
                self.__cursor.execute(Sql, Param)
            self.__dbHandle.commit()
            return self.__cursor.lastrowid
        except mysql.connector.Error as err:
            self.__dbError(err)
    
    
    def doInsert(self,aParam):
        if not aParam:
            return None;
        if not aParam.has_key(Config.S_TABLE):
            return None;
        if not aParam.has_key(Config.S_SEARCHFIELDS):
            return None;
        if aParam[Config.S_SEARCHFIELDS]=="":
            return None;
        if aParam[Config.S_SEARCHFIELDS]=="*":
            return None;
        
        
        
        fields="";
        values="";
        fieldsArr=aParam[Config.S_SEARCHFIELDS].split(",")
        for item in fieldsArr:
            tmp=item.split("=");
            fields=fields+str(tmp[0])+",";
            values=values+str(tmp[1])+",";
        fields=fields[:len(fields)-1];
        values=values[:len(values)-1];
        
        
        
        sSql="insert into %s (%s) values(%s)" %(aParam[Config.S_TABLE],fields,values);

        return self.executeAndGetId(sSql); 
        
    
    def doUpdate(self,aParam):
        if not aParam:
            return None;
        if not aParam.has_key(Config.S_TABLE):
            return None;
        if not aParam.has_key(Config.S_SEARCHFIELDS):
            return None;
        if aParam[Config.S_SEARCHFIELDS]=="":
            return None;
        if aParam[Config.S_SEARCHFIELDS]=="*":
            return None;
        
#        sFields=aParam[Config.S_SEARCHFIELDS].replace(",","=%s,")+"=%s";
        sSql="update %s set %s where 1=1" %(aParam[Config.S_TABLE],aParam[Config.S_SEARCHFIELDS]);
        if aParam.has_key(Config.S_SEARCHCONDITION) and aParam[Config.S_SEARCHCONDITION]!="":
            sSql=sSql+" and "+aParam[Config.S_SEARCHCONDITION];
        return self.executeAndGetId(sSql);    
        
        
        
    def doDelete(self,aParam):
        
        if not aParam:
            return None;
        if not aParam.has_key(Config.S_TABLE):
            return None;
        try:
            sSql="DELETE FROM %s where 1=1" %(aParam[Config.S_TABLE]);
            if aParam.has_key(Config.S_SEARCHCONDITION) and aParam[Config.S_SEARCHCONDITION]!="":
                sSql=sSql+" and "+aParam[Config.S_SEARCHCONDITION];
            return self.doExecute(sSql);       
        except mysql.connector.Error as err:
            self.__dbError(err)        
    def doSelect(self):
        pass
    def __dbError(self,errorMassges):
        LogInfo.writeLog("error", errorMassges)
if __name__ == '__main__':
    db=DbOperator();
    aParam={Config.S_TABLE:'Sq_UserInfo',Config.S_SEARCHFIELDS:"username='sss'",Config.S_SEARCHCONDITION:"cc='cc'"}
    print aParam
    db.doInsert(aParam);
