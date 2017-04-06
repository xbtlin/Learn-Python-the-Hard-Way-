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
        tag_level = '2'
        print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (str(famous_came),str(famous_others),str(famous_setup),str(famous_recommend),str(film_place),str(famous_came),str(internet_media),str(tradition_media),str(dianping_featured),str(tag_level))
        continue


if __name__ == '__main__':
    # st,fn=sys.argv
    # with open(fn,'rb') as fr:
    #     process(fr)
    process(sys.stdin)