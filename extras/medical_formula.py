#encoding=utf8
from sys import argv

if len(argv) != 5:
    print '''input age,height_cm,gender,xiejigan separated by space'''
    print '''依次输入 年龄,身高厘米,性别（1男，2女）,血肌酐值 以空格分开'''

script,age,height_cm,gender,xiejigan = argv

# inner_jigan_rm_rate = 0;
if int(gender)==1:
    std_wight = 50 + 2.3*(int(height_cm)/2.54 - 60)
    inner_jigan_rm_rate = (140 - int(age)) * std_wight / (72*int(xiejigan))
elif int(gender)==2:
    std_wight = 45.5 + 2.3*(int(height_cm)/2.54 - 60)
    inner_jigan_rm_rate = 0.85 * (140 - int(age)) * std_wight / (72 * int(xiejigan))
else:
    print "gender is 1 or 2, input error"
    exit(0)

print "内生肌酐清除率为： " + str(inner_jigan_rm_rate)