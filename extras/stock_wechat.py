# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

__author__ = 'ipreacher'

import time
import itchat
import datetime
import tushare as ts


stock_symbol = input('input stock code \n>  ')
price_low = input('input low_price \n>  ')
price_high = input('input high_price \n>  ')


# 登陆微信
def login():
    itchat.auto_login()


# 获取股价并发送提醒
def stock():
    time = datetime.datetime.now()    # 获取当前时间
    now = time.strftime('%H:%M:%S')
    data = ts.get_realtime_quotes(stock_symbol)    # 获取股票信息
    r1 = float(data['price'])
    name = data['name']
    r2 = name + ' ' + str(stock_symbol) + ' 的当前价格为 ' + str(r1)
    content = now + '\n' + r2
    itchat.send(content, toUserName='filehelper')
    # print itchat.get_contact()
    # flist = itchat.get_friends()
    # for item in flist:
    #     print item
    # print(content)
    # 设置预警价格并发送预警信息
    if r1 <= float(price_low):
        itchat.send('低于最低预警价格', toUserName='filehelper')
        print('低于最低预警价格')
    elif r1 >= float(price_high):
        itchat.send('高于最高预警价格', toUserName='filehelper')
        print('高于最高预警价格')
    else:
        itchat.send('价格正常', toUserName='filehelper')
        print('价格正常')


# 每 3 秒循环执行
if __name__ == '__main__':
    # login()
    while True:
        try:
            stock()
            time.sleep(3)
        except KeyboardInterrupt:
            itchat.send('Stock_WeChat 已执行完毕！\n'
                '更多有意思的小玩意，请戳---->\n'
                '[https://github.com/ipreacher/tricks]',
                toUserName='filehelper')
            print('Stock_WeChat 已执行完毕！\n'
                '更多有意思的小玩意，请戳---->\n'
                '[https://github.com/ipreacher/tricks]')
            break