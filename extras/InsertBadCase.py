#!/usr/local/bin/python
# coding=utf-8
import sys
import csv
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
# from Writer import Writer

import libPythonKms

reload(sys)


class MysqlWriter():
    """Mysql 数据写回"""

    meta_need = ['host', 'port', 'user', 'passwd', 'db']

    def __init__(self, **meta):
        self.meta = {}
        # super(Writer, self).__init__()
        for item in self.meta_need:
            if item not in meta.keys():
                raise Exception('meta not enough')
            self.meta[item] = meta[item]

        self.meta['charset'] = meta.get('charset', 'utf8')

        self.connect = None

    def _connect(self):
        if self.connect:
            return
        self.connect = MySQLdb.connect(**self.meta)
        # 强制不自动commit
        self.connect.autocommit(0)

    def before_write(self):
        pass

    def after_write(self):
        pass

    def write(self, sql, iscommit=False):
        self.before_write()
        self.write_raw(sql, iscommit)
        self.after_write()

    def write_raw(self, sql, iscommit=False):
        self._connect()
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute(sql)
        except Exception, e:
            self.connect.rollback()
            raise Exception(str(e))
        else:
            if iscommit:
                self.connect.commit()
        self.cursor.close()

    def query(self, sql):
        self._connect()
        self.cursor = self.connect.cursor()
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.cursor.close()

        return result

if __name__ == '__main__':
    cis = {
        # 'host': "hh",
        'port': 5002,
        'db': 'tags',
        # 'user': 'hh',
        # 'passwd': 'hh'
    }

    # SQL = "insert into poi_tag(`%s`) values(\"%s\")"
    # SQL = "updated poi_tag set whereExpression='mt_main_poi_id IS NOT NULL AND mt_poi_cate1_id=226 AND poi_close_status=0 AND mt_main_poi_id=poi_id AND partition_chain=\'mt\'' where owner='wujunchao'"
    writer = MysqlWriter(**cis)

    # path = "badcases.csv"
    #
    # fopen = csv.DictReader(file(path))
    # SQL = "insert into shop_test_poi_tags(`poi_id`,`tag_name`,`value`,`type`,`modify_time`) VALUES(%d,%s,%s,%d,%s)"
    # for row in fopen:
        # poi_id = row['poi_id']
        # cate3name = row['cate3name']
        # today = datetime.datetime.today().strftime('%Y-%m-%d')
        # getCate3Sql = "SELECT poi_front_cate3_id from dim_mining_shop_tags_aggregation_d WHERE poi_id = "+poi_id
        # results = []
        # poi_front_cate3_id = ''
        # try:
        #     results = writer.query(getCate3Sql)
        # except Exception, e:
        #     print e
        # for row in results:
        #     poi_front_cate3_id = row['poi_front_cate3_id']
        #
        # sql1 = SQL % (int(poi_id),"poi_front_cate3_id",str(poi_front_cate3_id),1,str(today))
        # sql2 = SQL % (int(poi_id),"poi_front_cate3_name",str(cate3name),1,str(today))

    sql3 = "INSERT INTO Table shop_test_poi_tags(poi_id,tag_name,value,type,modify_time)  VALUES (97758745,'poi_front_cate3_id','10226',1,'2017-02-03'), (115816744,'poi_front_cate3_id','10226',1,'2017-02-03'), (5826801,'poi_front_cate3_id','10226',1,'2017-02-03'), (77663384,'poi_front_cate3_id','10226',1,'2017-02-03'), (97758745,'poi_front_cate3_name','潮州菜',1,'2017-02-03'), (115816744,'poi_front_cate3_name','潮州菜',1,'2017-02-03'), (5826801,'poi_front_cate3_name','潮州菜',1,'2017-02-03'), (77663384,'poi_front_cate3_name','潮州菜',1,'2017-02-03')"
    try:
        writer.write(sql3, True)
        # writer.write(sql2, True)
    except Exception, e:
        print e
