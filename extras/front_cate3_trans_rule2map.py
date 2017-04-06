#!/bin/python
# encoding=utf8

from sys import *

def process(filein,fileout1,fileout2,f3,f4):
    id2cate_set=set()
    id3cate_set=set()
    cate2name_set=set()
    cate3name_set=set()
    with open(filein,'rb') as fr:
        for line in fr:
            try:
                cols=line.strip().split('\t')
                assert(len(cols)==5)


            except Exception,e:
                stderr.write(str(e))
                stderr.write("Error: Split error!!! \n")
                stderr.write(line)
                continue

            try:
                cate2name=cols[1]
                cate3name=cols[3]
                cate2name_set.add(cate2name)
                cate3name_set.add(cate3name)
                if '含' in cols[4]:
                    continue
                cate2_ids=cols[0].split('&')
                for id in cate2_ids:
                    item=id+':'+'u\''+cate2name+'\''
                    id2cate_set.add(item)

                cate3_ids=cols[2].strip().split('&')
                for id in cate3_ids:
                    if id>'0':
                        item=id+':'+'u\''+cate3name+'\''
                        id3cate_set.add(item)
                    else:
                        continue
            except Exception,e:
                stderr.write(e)
                continue
    fr.close()
    # fw1=open(fileout1,'w')
    # for item in id2cate_set:
    #     fw1.write(item+', ')
    # fw1.close()
    #
    # fw2=open(fileout2,'w')
    # for item in id3cate_set:
    #     fw2.write(item+', ')
    # fw2.close()

    fw3=open(f3,'w')
    i=1
    for item in cate2name_set:
        fw3.write('u\''+item+'\': '+str(i)+', ')
        i=i+1

    fw4=open(f4,'w')
    i=201
    for item in cate3name_set:
        fw4.write('u\''+item+'\': '+str(i)+', ')
        i=i+1

if __name__=='__main__':
    if(len(argv) < 6):
        print "need input 5 parameter: filein, fileout1, fileout2!"
    script,filein,fileout1,fileout2,f3,f4=argv
    process(filein,fileout1,fileout2,f3,f4)