# encoding=utf8
import sys
import MySQLdb
from SqlWriter import MysqlWriter
reload(sys)
sys.setdefaultencoding('utf8')
import itchat

def login():
    itchat.auto_login()

def writeFriendInfo(meta):
    writer = MysqlWriter(**meta)
    flist = itchat.get_friends()
    itchat.send("哈哈哈哈。。。牛逼了", toUserName='wyb52419')
    for item in flist:
        key_list = []
        key_list.append("remark_name")
        key_list.append("nick_name")
        key_list.append("sex")
        key_list.append("city")
        key_list.append("signature")
        key_list.append("reserve")
        value_list = []
        value_list.append(item["RemarkName"])
        value_list.append(item["NickName"])
        value_list.append(str(item["Sex"]))
        value_list.append(item["City"])
        value_list.append(item["Signature"])
        value_list.append(item["Province"])
        try:
            sql = "INSERT INTO friend_info (`" + '`,`'.join(key_list) + "`) VALUES(\"" + "\",\"".join(value_list) + "\")"
            writer.write(sql, True)
        except Exception, e:
            print e
            continue

if __name__ == "__main__":

    friend = {
        'host': '127.0.0.1',
        'port': 3306,
        'db': 'job',
        'user': 'root',
        'passwd': '1234'
    }

    login()
    writeFriendInfo(friend)