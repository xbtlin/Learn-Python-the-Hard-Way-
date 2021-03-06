# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

TYPE3MAP = {
    11: u'中式快餐', 2087: u'麻辣烫', 183: u'面馆', 1963: u'面馆', 1974: u'面馆', 1976: u'面馆', 1943: u'包子/粥', 1942: u'包子/粥',
    251: u'包子/粥', 2017: u'包子/粥', 2082: u'饺子馄钝', 2083: u'饺子馄钝', 2093: u'生煎锅贴', 214: u'生煎锅贴', 2095: u'鸭脖卤味',
    2089: u'炸鸡炸串', 1954: u'地方小吃', 1955: u'地方小吃', 1956: u'地方小吃', 1957: u'地方小吃', 1962: u'地方小吃', 1964: u'地方小吃',
    1977: u'地方小吃', 2022: u'地方小吃', 2023: u'地方小吃', 2024: u'地方小吃', 2025: u'地方小吃', 1944: u'米粉&米线', 1945: u'米粉&米线',
    1946: u'米粉&米线', 1947: u'米粉&米线', 1948: u'米粉&米线', 1949: u'米粉&米线', 1950: u'米粉&米线', 1951: u'米粉&米线', 252: u'汤类',
    1952: u'汤类', 1953: u'汤类', 2018: u'汤类', 2019: u'汤类', 23: u'日本料理', 2042: u'日本料理', 2041: u'日本料理', 24: u'韩国料理',
    170: u'日式自助', 317: u'铁板烧', 2040: u'寿司', 1993: u'烤鸭', 1961: u'炸酱面', 1906: u'浙菜',
    1908: u'浙菜', 1909: u'浙菜', 1910: u'浙菜', 1911: u'浙菜', 2014: u'浙菜', 1904: u'杭帮菜', 1905: u'宁波菜', 1913: u'苏菜',
    1915: u'苏菜', 1917: u'苏菜', 1918: u'苏菜', 1912: u'南京菜', 1914: u'淮扬菜', 2015: u'无锡菜', 1916: u'大闸蟹', 153: u'串串香',
    1921: u'川味火锅', 1922: u'川味火锅', 237: u'川味火锅', 239: u'涮羊肉', 241: u'鱼火锅', 242: u'羊蝎子', 1894: u'云南火锅', 1929: u'云南火锅',
    1930: u'云南火锅', 1931: u'云南火锅', 313: u'韩式火锅', 210: u'自助火锅', 323: u'小火锅', 1932: u'小火锅', 1933: u'小火锅',
    1925: u'牛肉火锅', 2035: u'砂锅火锅', 1928: u'特色火锅', 169: u'自助海鲜', 171: u'自助烧烤', 2032: u'烤鱼',
    2001: u'香锅', 2002: u'酸菜鱼', 2000: u'江湖菜', 13: u'冰淇淋', 1901: u'甜品', 1902: u'甜品', 256: u'甜品', 1900: u'甜品', 1903: u'甜品',
    179: u'甜品', 249: u'甜品', 2112: u'甜品', 660: u'零食', 661: u'保健品', 662: u'栗子/干果', 665: u'水果', 666: u'生鲜', 246: u'泰国菜',
    247: u'印度菜', 1938: u'西式快餐', 2016: u'西式快餐', 19: u'法国菜', 20: u'意大利菜', 2070: u'墨西哥菜', 2062: u'美国菜', 1848: u'汉堡',
    1939: u'比萨', 1940: u'牛排', 322: u'西班牙菜', 181: u'中东菜', 1941: u'西式正餐', 2059: u'西式正餐', 2043: u'烤翅', 2044: u'烤串',
    220: u'本地烤肉', 318: u'韩式烤肉', 233: u'客家菜', 2119: u'潮州菜', 2117: u'顺德菜', 2115: u'茶餐厅', 2114: u'燕翅鲍',
    2116: u'广州菜', 2120: u'烧腊', 1923: u'海鲜火锅'
}

TYPE2MAP = {
    10: [u'小吃快餐'], 23: [u'日韩料理'], 24: [u'日韩料理'], 318: [u'日韩料理',u'烧烤'], 239: [u'北京菜',u'火锅'], 27: [u'北京菜'], 1961: [u'北京菜'], 30: [u'江浙菜'], 174: [u'西北菜'],
    175: [u'东北菜'], 201: [u'火锅'], 210: [u'火锅',u'自助餐'], 202: [u'自助餐'], 170: [u'自助餐',u'日韩料理'], 228: [u'山东菜'], 229: [u'川菜'], 230: [u'湘菜'], 231: [u'湖北菜'],
    232: [u'台湾菜'], 235: [u'新疆菜'], 1978: [u'咖啡厅'], 1987: [u'咖啡厅'], 262: [u'咖啡厅'], 1988: [u'咖啡厅'], 1979: [u'咖啡厅'], 1984: [u'咖啡厅'],
    1986: [u'咖啡厅'], 1982: [u'咖啡厅'], 2030: [u'咖啡厅'], 2031: [u'咖啡厅'], 1981: [u'咖啡厅'], 1985: [u'咖啡厅'], 1980: [u'咖啡厅'], 1983: [u'咖啡厅'],
    2110: [u'饮品'], 2113: [u'饮品'], 2111: [u'饮品'], 1901: [u'面包甜点'], 1902: [u'面包甜点'], 256: [u'面包甜点'], 1900: [u'面包甜点'], 1903: [u'面包甜点'],
    179: [u'面包甜点'], 249: [u'面包甜点'], 13: [u'面包甜点'], 12: [u'蛋糕'], 255: [u'食品保健'], 257: [u'水果生鲜'], 298: [u'江西菜'], 299: [u'山西菜'], 300: [u'徽菜'], 301: [u'闽菜'],
    302: [u'西藏菜'], 303: [u'河南菜'], 304: [u'海南菜'], 306: [u'天津菜'], 307: [u'广西菜'], 308: [u'东南亚菜'], 309: [u'西餐'], 315: [u'烧烤'], 171: [u'烧烤',u'自助餐'],
    319: [u'粤菜'], 2162: [u'河北菜'], 9: [u'海鲜'], 1923: [u'海鲜',u'火锅'], 169: [u'海鲜',u'自助餐'], 2037: [u'江河湖鲜'], 2038: [u'江河湖鲜'], 2039: [u'江河湖鲜'],
    2088: [u'小龙虾'], 2047: [u'特色菜'], 2048: [u'特色菜'], 2049: [u'特色菜'], 2050: [u'特色菜'], 2052: [u'特色菜'], 2053: [u'特色菜'], 2054: [u'特色菜'],
    2055: [u'特色菜'], 223: [u'创意菜'], 2046: [u'农家菜'], 2051: [u'清真菜'], 2045: [u'家常菜'], 120: [u'私房菜'], 16: [u'素菜'], 35: [u'云南菜'], 36: [u'贵州菜'],
    184: [u'其他餐饮']

}

FRONT_TYPE2_ID_NAME = {
    u'贵州菜':10044, u'小吃快餐':10021, u'西藏菜':10027, u'江河湖鲜':10047, u'广西菜':10006, u'蛋糕':10028, u'饮品':10050, u'家常菜':10002, u'粤菜':10036, u'烧烤':10038, u'清真菜':10035, u'自助餐':10024, u'海鲜':10004, u'东北菜':10014, u'咖啡厅':10016, u'火锅':10033, u'北京菜':10009, u'小龙虾':10293, u'江西菜':10020, u'天津菜':10043, u'水果生鲜':10015, u'农家菜':10039, u'云南菜':10066, u'食品保健':10008, u'私房菜':10012, u'山西菜':10013, u'闽菜':10005, u'东南亚菜':10011, u'其他餐饮':10072, u'西餐':10023, u'特色菜':10074, u'西北菜':10040, u'台湾菜':10010, u'素菜':10025, u'山东菜':10018, u'新疆菜':10031, u'创意菜':10034, u'河北菜':10030, u'川菜':10003, u'湖北菜':10026, u'江浙菜':10037, u'面包甜点':10085, u'徽菜':10001, u'河南菜':10029, u'日韩料理':10019, u'海南菜':10042, u'湘菜':10022
}

FRONT_TYPE3_ID_NAME = {
    u'生煎锅贴':10266, u'串串香':10218, u'甜品':10203, u'杭帮菜':10234, u'潮州菜':10226, u'水果':10233, u'冰淇淋':10286, u'顺德菜':10289, u'自助火锅':10263, u'比萨':10224, u'烤翅':10260, u'香锅':10219, u'麻辣烫':10311, u'西式快餐':10272, u'星级酒店自助':10202, u'苏菜':10239, u'鸭脖卤味':10303, u'日式自助':10258, u'牛排':10312, u'炸酱面':10288, u'寿司':10310, u'居酒屋':10334, u'韩国料理':10335, u'泰国菜':10221, u'米粉&米线':10337, u'川味火锅':10227, u'砂锅火锅':10339, u'中式快餐':10298, u'大闸蟹':10216, u'烤鸭':10296, u'包子/粥':10343, u'炸鸡炸串':10307, u'意大利菜':10244, u'南京菜':10264, u'本地烤肉':10268, u'酸菜鱼':10238, u'韩式火锅':10280, u'江湖菜':10243, u'烧腊':10207, u'韩式烤肉':10229, u'云南火锅':10251, u'日本料理':10354, u'羊蝎子':10228, u'牛肉火锅':10308, u'饺子馄钝':10357, u'汤类':10358, u'自助烧烤':10257, u'特色火锅':10360, u'烤鱼':10225, u'铁板烧':10230, u'茶餐厅':10292, u'印度菜':10262, u'宁波菜':10212, u'涮羊肉':10291, u'焖锅':10297, u'墨西哥菜':10237, u'淮扬菜':10254, u'海鲜火锅':10283, u'浙菜':10245, u'广州菜':10270, u'鱼火锅':10276, u'栗子/干果':10290, u'地方小吃':10278, u'中东菜':10273, u'汉堡':10304, u'燕翅鲍':10206, u'零食':10301, u'自助海鲜':10241, u'美国菜':10274, u'客家菜':10306, u'无锡菜':10284, u'西班牙菜':10231, u'面馆':10385, u'西式正餐':10386, u'小火锅':10294, u'法国菜':10250, u'烤串':10285, u'生鲜':10269, u'保健品':10222
}

def process(input):
    for line in input:
        try:
            cols = line.strip().split("\t")
            assert (len(cols) == 4)
        except Exception:
            sys.stderr.write("Error: Split error!!! \n")
            continue

        try:
            if int(cols[2]) in TYPE2MAP.keys():
                front_cate2_name_arr = TYPE2MAP[int(cols[2])]
            elif int(cols[1]) in TYPE2MAP.keys():
                front_cate2_name_arr = TYPE2MAP[int(cols[1])]
            else:
                front_cate2_name_arr = [u'其他餐饮']

            front_cate2_id_arr=[]
            for index in range(len(front_cate2_name_arr)):
                if front_cate2_name_arr[index] in FRONT_TYPE2_ID_NAME.keys():
                    front_cate2_id_arr.append(FRONT_TYPE2_ID_NAME[front_cate2_name_arr[index]])
                else:
                    front_cate2_id_arr.append(-1)

            front_cate3_name = ''
            if int(front_cate2_id_arr[0]) == 10033 and '焖锅' in cols[3]:
                front_cate3_name = u'焖锅'
            elif int(cols[2]) in TYPE3MAP.keys():
                front_cate3_name = TYPE3MAP[int(cols[2])]

            if front_cate3_name in FRONT_TYPE3_ID_NAME.keys():
                front_cate3_id = FRONT_TYPE3_ID_NAME[front_cate3_name]
            else:
                front_cate3_name = front_cate2_name_arr[0]
                front_cate3_id = front_cate2_id_arr[0]

            for index in range(len(front_cate2_name_arr)):
                print "%s\t%s\t%s\t%s\t%s\t%s" % (
            str(cols[0]), str(front_cate2_id_arr[index]), str(front_cate2_name_arr[index]), str(front_cate3_id), str(front_cate3_name),
            str(1.0))

        except Exception, e:
            sys.stderr.write(str(e))
            sys.stderr.write("Error: Input error!!!\n")
            continue

if __name__ == '__main__':
    process(sys.stdin)