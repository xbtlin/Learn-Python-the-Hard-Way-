# coding=utf-8
import os


def replace(filePath, w2u):
    try:
        oldfile = open(filePath, "rb+")  # 这里必须用b打开
        path, name = os.path.split(filePath)
        newfile = open(r'/Users/linxuan/Desktop/new.py', 'wb+')  # 绝对路径

        old = b''
        new = b''
        if w2u == True:
            old = b'\r'
            new = b''
        else:
            old = b'\n'
            new = b'\r\n'

        data = b''
        while (True):
            data = oldfile.read(200)
            newData = data.replace(old, new)
            newfile.write(newData)
            if len(data) < 200:
                break
        newfile.close()
        oldfile.close()

    except IOError as e:
        print(e)


if __name__ == "__main__":
    # print("请输入文件路径：")
    filePath = r'/Users/linxuan/github/Learn-Python-the-Hard-Way-/extras/poi_front_type_map.py'  # 绝对路径
    replace(filePath, True)  # 这个改为True就可以实现\n变成\r\n