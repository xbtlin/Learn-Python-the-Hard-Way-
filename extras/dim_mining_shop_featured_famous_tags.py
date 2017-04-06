# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def process(input):
    for line in input:
        famous_others = 'none'
        famous_setup = 'none'
        famous_recommend = 'none'
        film_place = 'none'
        famous_came = 'none'
        internet_media = 'none'
        tradition_media = 'none'
        dianping_featured = 'none'
        tag_level = 2
        try:
            cols = line.strip().split("\t")
            assert (len(cols) == 6)
        except Exception:
            sys.stderr.write("Error: Split error!!! \n")
            continue

        try:
            tagtype = cols[2]
            subtype = cols[3]
            tags = cols[4]
            shortintro = cols[5]

            ct=0
            taglist=[u'公众号',u'微博',u'新浪美食',u'马蜂窝',u'携程']
            if subtype==u'媒体推荐':
                for tag in taglist:
                    if tag in tags:
                        ct = ct+1

            if subtype in {u'名人投资', u'名人使用', u'名人主题',u'名人母校', u'名人建造', u'名人合照', u'名人故居', u'名人事件', u'名人题字'}:
                famous_others = str(shortintro)
            elif subtype in {u'名人光顾'}:
                famous_came = str(shortintro)
            elif subtype in {u'名人开店'}:
                famous_setup = str(shortintro)
            elif subtype in {u'名人推荐'}:
                famous_recommend=str(shortintro)
            elif subtype in {u'影视作品取景地'}:
                film_place = str(shortintro)
            elif subtype == u'媒体推荐' and tags == u'点评精选榜单':
                dianping_featured=str(shortintro)
            elif subtype == u'媒体推荐' and ct>0:
                internet_media=str(shortintro)
            elif subtype == u'媒体推荐':
                tradition_media = str(shortintro)

            print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (str(cols[0]),str(famous_others),str(famous_setup),str(famous_recommend),str(film_place),str(famous_came),str(internet_media),str(tradition_media),str(dianping_featured),str(tag_level))
        except Exception, e:
            sys.stderr.write(str(e))
            sys.stderr.write("Error: Input error!!!\n")
        continue


if __name__ == '__main__':
    # st,fn=sys.argv
    # with open(fn,'rb') as fr:
    #     process(fr)
    process(sys.stdin)