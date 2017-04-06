# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def process(input):
    for line in input:
        try:
            cols = line.strip().split("\t")
            assert (len(cols) >= 3)
            if len(cols) == 3:
                cols.append('none')
        except Exception:
            sys.stderr.write("Error: Split error!!! \n")
            continue

        try:
            poi_name = cols[2]
            back_cate3_name = cols[1]
            brand_name=cols[3]
            front_cate3_name=''
            if brand_name in BRAND_NAME.keys() and BRAND_NAME[brand_name][0]==back_cate3_name:
                front_cate3_name=front_cate3_name+BRAND_NAME[brand_name][1]
            else:
                for k in POINAME_MAP.keys():
                    if k in poi_name:
                        name_list = POINAME_MAP[k]
                        if len(name_list) > 2 and name_list[2] in poi_name:
                            continue;
                        elif name_list[0] == back_cate3_name:
                            front_cate3_name=name_list[1]
                if front_cate3_name=='':
                    continue

            print "%s\t%s\t%s\t%s\t%s" % (str(cols[0]), str(cols[1]), str(cols[2]), str(cols[3]), str(front_cate3_name))

        except Exception, e:
            sys.stderr.write(str(e))
            sys.stderr.write("Error: Input error!!!\n")
        continue


if __name__ == '__main__':
    script,filename=sys.argv
    with open(filename,'rb') as fr:
        process(fr)
    # process(sys.stdin)