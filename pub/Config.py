#encoding=utf8
'''
Created on 2012-9-28

@author: Administrator

'''
import os
import sys
import time



class Config(object):
    """
        全局变量类,其中常量类型为首字母代表，例如首字母为D则为字典类型
        数据类型说明：
        D        字典
        I          数字
        T        表
        S        字符串
    """
    CONFIG_KEY_STRING = "sequence_app_configure"
    
#    系统当前时间常量
    I_SYS_ZERO = 0
#    系统零常量

    I_SYS_ONE = 1
#    系统一常量

    S_SYS_NONE = None
#    系统None常量
    B_SYS_DEBUG = True
#    系统调试变量
    B_SYS_WRITE_LOG=False
    B_SYS_TRACE = True
    LOG_FILE_NAME = "logs/%s.log"
#    是否打印出回逆信息
#是否写系统日志
#dsaffdfsdfs
    D_USER_DICT = {}
# [Users]
#    用户字典
#    D_USER_DICT = {
#                 "geminiblue":UserObj,
#                 }

    I_USER_STATE_ONLINE = 1
    #  用户状态  1 当前用户在线

    I_USER_STATE_OFFLINE = 0
    #  用户状态  0  当前用户离线    
    B_USER_LOGIN_OK = True
    # 用户登录成功
    B_USER_LOGIN_ERR = False
    #用户登录失败
    I_USER_GAME_STATE_OK = 1
#  用户游戏状态    1 当前用户游戏中
    I_USER_GAME_STATE_OVER = 0
#  用户游戏状态    0 当前用户被淘汰
    I_USER_GAME_STATE_SEE = 2    
#  用户游戏状态    2 旁观用户，代表下局可参加游戏

    I_USER_GAME_STATE_INIT= -1;
    #用户不在任何房间里
    
    I_USER_IS_ROOM_OWNER = 1
#        当前用户是否是房主   1 为是    
    I_USER_NOT_IS_ROOM_OWNER = 0
#        当前用户是否是房主    0 为否
    I_USER_CHECK_FLAG_YES = 1
#  当前用户被添加好友时是否需要验证 1 是
    I_USER_CHECK_FLAG_NO = 0
#  当前用户被添加好友时是否需要验证 0 否
    I_USER_SEARCH_FLAG_NONE = 0
#    无法搜索到用户
    I_USER_SEARCH_FLAG_NICKNAME = 1
#    只能通过用户名搜索到用户
    I_USER_SEARCH_FLAG_USERNAME = 2
#    只能通过电话搜索到
    I_USER_SEARCH_FLAG_TEL = 4
#    可以通过任何条件搜索到此用户
    I_USER_SEARCH_FLAG_ALL = 8
#    任何条件可搜索到
    I_USER_NOT_FOUND = 1001
#    用户名错误
    I_USER_PASSWORD_ERROR = 1002
#    用户密码错误
    I_USER_LOGIN_OK = 1000
#    用户登录成功
    I_USER_REGISTER_OK = 1010
#    用户注册成功
    I_USER_REGISTER_USERNAME_FOUND = 1011
#    用户注册用户名已存在
    I_USER_REGISTER_USERNAME_ERROR = 1012
#    用户注册用户名不合法
    I_USER_REGISTER_PASSWORD_ERROR = 1013
#    用户注册密码不合法    
    I_USER_CHANGE_PASSWORD_OK = 1020
#    用户修改密码成功
    I_USER_OLD_PASSWORD_WRONG = 1021
#    用户旧密码不符
    I_USER_NICK_NAME_FOUND = 1031
#    用户昵称重复
    I_USER_MODIFAN_INFO_OK = 1030
#    用户修改信息成功
    I_USER_MODIFAN_INFO_ERROR = 1032
#    用户修改信息失败

    I_USER_FIND_INFO_SUSS = 1040
#    查不到用户
    I_USER_FIND_INFO_ERROR = 1041
#    查不到用户


    D_ROOM_DICT = {}
#  [Rooms]       
#    房间字典
#D_ROOM_DICT = {
#                'roomId':roomObj
#             }    

    I_ROOM_PRI_PUB = 0
    #  房间权限：    0  公开房间
    I_ROOM_PRI_PRO = 1
    #  房间权限：   1 私有房间

    I_ROOM_TYPE_SYSTEM = 0
    #  房间类型： 0 系统房间  
    I_ROOM_TYPE_USER = 1
    #  房间类型： 1 用户房间  

    I_ROOM_STATE_READY = 0
    #  房间状态  0 准备状态 
    I_ROOM_STATE_START = 1
    #  房间状态  1 开始状态（游戏中）
    I_ROOM_STATE_OVER = 2
    #  房间状态  2 结束状态（游戏结束） 
    I_ROOM_UP_LIMIT = 50
    #房间人数上限
    I_ROOM_LIST_NULL = 1041
    #房间列表为空
    I_ROOM_LIST_OK = 1040
    #取得房间列表成功
    I_ROOM_LIST_ERROR = 1042
    #取得房间列表失败
    T_USER_INFO = "Sq_UserInfo"
    #  用户信息表

    T_USER_FRIENDS = "Sq_UserFriendsRelation"
    #    用户好友信息表

    T_MESSAGE = "Sq_message"
    #    消息信息表

    T_ROOMS = "Sq_room"
    #    房间信息表

    T_FEEDBACK = "Sq_Feedback"
    #    反馈信息表

    T_IDIOM = "Sq_idiom"
    #    成语信息表

    T_IDIOMLETTERS = "Sq_idiomletters"
#    成语首字信息表


    S_SEARCHFIELDS = "SearchFields";
    #sql中要搜索字段的的key
    S_SEARCHCONDITION = "SearchCondition";
    #sql中要搜索条件的key
    S_RESULTROW = "resultRow";
    #sql中要搜索结果条目key
    S_TABLE = "table";
    #sql中要搜索表的key
    S_ORDERBY = "orderby"
    S_FETCH_ALL = "fetchAllData"
    #sql中的排序字段
    S_LIMIT = "limit"
    HAS_JOIN=""
    EARTH_RADIUS_METER = 6378137.0 
    #经纬度常量
    S_PINYIN_DB_FILE = "../data/Mandarin.dat"
    SYS_ERROR_COMMAND = "SYS#%s#%s"
    SYS_COMMAND_NOT_FOUND = 404
    SYS_CALL_COMMAND_ERROR = 500
    I_MAX_DISTANCE=1000
    I_MESSAGE_ADD_OK=4000
    I_FEEDBACK_ADD_OK=5000
    
    

    
    
    CommandMap = {
                "PIS":("PIS","PISClass"),  
                "UL":("UL","ULClass"), #用户登录
                "UR":("UR","URClass"), #用户注册
                "PIS":("PIS","PISClass"),
                "RI":("RI","RIClass"),
                "UPM":("UPM","UPMClass"),
                "UIM":("UIM","UIMClass"),
                "RU":("RU","RUClass"), #房间用户列表
                "RGA":("RGA","RGAClass"), #用户加入房间
                "RISG":("RISG","RISGClass"), #开始游戏
                "RIG":("RIG","RIGClass"), #接龙过程
                "RIC":("RIC","RICClass"),#使用道具
                "RIFU":("RIFU","RIFUClass"),#邀请游戏玩家列表
                "RINU":("RINU","RINUClass"),#附近玩家       
                "RIFA":("RIFA","RIFAClass"), #邀请玩家
                "RIFAC":("RIFAC","RIFACClass"),#反馈邀请        
                "RIUE":("RIUE","RIUEClass"),#玩家放弃游戏
                "RIKO":("RIKO","RIKOClass"),#房主踢人
                "RISO":("RISO","RISOClass"),#主动退出房间
                "UFL":("UFL","UFLClass"),#好友列表
                "UFFA":("UFFA","UFFAClass"),#添加好友
                "UFSA":("UFSA","UFSAClass"),#好友验证
                "USD":("USD","USDClass"),#玩家详情
                "UFNU":("UFNU","UFNUClass"),#附近玩家
                "UFC":("UFC","UFCClass"),#好友聊天
                "UFS":("UFS","UFSClass"),#搜索玩家
                "UPS":("UPS","UPSClass"),#隐私设置
                "SVC":("SVC","SVCClass")#检测系统版本
                
    }
#    命令类对应关系
    cfg = {
#           数据库连接配置
           "DbConnectString" :{
                                                'user': 'root',
                                                'password': '1234567',
                                                'host': '127.0.0.1',
                                                'database': 'sequence',
                                                'raise_on_warnings': True, },
    
    }
    
    ERROR_MESSAGE_ROOM_NULL = "房间字典为空";
    #房间字典为空
    ERROR_MESSAGE_ROOM_DETAIL_NULL = "在房间字典无法找到该房间 ";
    #房间字典为空
    ERROR_MESSAGE_USER_DETAIL_NULL = "在用户字典无法找到该用户";
  
    
    ERROR_MESSAGE_ROOM_OWER_NULL = "用户非此房间的房主";
    
    ERROR_MESSAGE_ROOM_USER_NO = "非此房间的用户";
    
    
    
    
    ROOM_MESSAGE_CODE_ADD_FILL = 2001;
    #加入房间失败
    ROOM_MESSAGE_CODE_ADD_SUSS = 2000;
    #加入房间成功
    ROOM_MESSAGE_CODE_UPPER_LIMIT = 2002;
    #达到上限人数
    
    ROOM_MESSAGE_CODE_START_LOWER_LIMIT = 2003;    
    #未达到游戏人员
    ROOM_MESSAGE_CODE_START_SUSS = 2004;    
    #未达到游戏人员
    
    
    ROOM_MESSAGE_CODE_IDIOM_SUSS = 2010;    
    #接龙成功    
    ROOM_MESSAGE_CODE_IDIOM_USED = 2011;    
    #已使用过词
    ROOM_MESSAGE_CODE_IDIOM_NO = 2012;    
    #非成语
    ROOM_MESSAGE_CODE_IDIOM_FAIL = 2013;    
    #首尾不对
    

    
    
   

    
    EXIT_CMD = "EXIT";
    #socket断开
    
    pinYin = None;
    #拼音对象
    COMMENT_STYLE_HUSH=0;
    #嘘他
    COMMENT_STYLE_UP=1;
    #加油
    COMMENT_STYLE_PRAISE=2;
    #赞
    COMMENT_STYLE_QUICK=3;
    #快
    



    

