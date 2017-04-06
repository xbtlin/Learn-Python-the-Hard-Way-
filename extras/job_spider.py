#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib2
import random
import MySQLdb
import json
from bs4 import BeautifulSoup
from SqlWriter import MysqlWriter
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#Some User Agents
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]

def job_spider(meta, url_page):
    """
    爬取今日头条招聘页面的研发岗信息
    """
    try:
        req = urllib2.Request(url_page,headers=hds[random.randint(0,len(hds)-1)])
        source_code = urllib2.urlopen(req,timeout=10).read()
        plain_text=unicode(source_code)#,errors='ignore')
        soup = BeautifulSoup(plain_text)

        newDictionary = json.loads(str(plain_text))
    except (urllib2.HTTPError, urllib2.URLError), e:
        print e
        exit(-1)
    except Exception,e:
        print e
        exit(-1)


    writer = MysqlWriter(**meta)

    pos_list=newDictionary["positions"]
    for pos_dict in pos_list:
        key_list=[]
        value_list=[]
        try:
            for key,value in pos_dict.iteritems():
                # print "\t,"+"`"+key+"` " + "varchar(60) DEFAULT NULL"
                key_list.append(str(key))
                value_list.append(str(value).replace(",","."))
            sql = "INSERT INTO job_info4 (`"+'`,`'.join(key_list)+"`) VALUES(\""+ "\",\"".join(value_list)+"\")"
            writer.write(sql,True)
        except Exception, e:
            print e
            continue

if __name__=="__main__":
    cis = {
        'host': '127.0.0.1',
        'port': 3306,
        'db': 'job',
        'user': 'root',
        'passwd': '1234'
    }

    # cis = {
    #     'host': '10.4.241.144',
    #     'port': 5002,
    #     'db': 'edlp',
    #     'user': 'q3boy',
    #     'passwd': 'q3girl'
    # }

    url=u"https://job.toutiao.com/recruitment/positions/?type=1&summary_id=&sequence=&city=&name=&limit=10000&offset=0"
    url2 = u"https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput="
    url3 = u"https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput="
    url4 = u"https://job.alibaba.com/zhaopin/positionList.htm"
    url5 = u"http://talent.baidu.com/external/baidu/index.html#/social/2"
    job_spider(cis,url5)