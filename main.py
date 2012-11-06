#encoding=utf-8
from models.DbOperator import DbOperator
from pub.Config import Config
if __name__ == '__main__':
    db=DbOperator();
    aParam={Config.S_TABLE:'Sq_UserInfo',Config.S_SEARCHFIELDS:"username='sss'",Config.S_SEARCHCONDITION:"cc='cc'"}
    print aParam
    print db.doInsert(aParam);