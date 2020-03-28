from get_index import BaiduIndex
import pandas as pd
import csv
import time
import random
if __name__ == "__main__":
    keywords = ['孔子']

    PROVINCE_CODE = {'山东': '901', '贵州': '902', '江西': '903', '重庆': '904', '内蒙古': '905', '湖北': '906', '辽宁': '907', '湖南': '908', '福建': '909', '上海': '910', '北京': '911', '广西': '912', '广东': '913', '四川': '914', '云南': '915', '江苏': '916', '浙江': '917', '青海': '918', '宁夏': '919', '河北': '920', '黑龙江': '921', '吉林': '922', '天津': '923', '陕西': '924', '甘肃': '925', '新疆': '926', '河南': '927', '安徽': '928', '山西': '929', '海南': '930', '台湾': '931', '西藏': '932', '香港': '933', '澳门': '934'}

    years = ['2019']

    result = []
    yearIndex = 0;
    for yearIndex in range(len(years)):
        for keys,value in PROVINCE_CODE.items():
            startDay = years[yearIndex]+'-01-01'
            endDay = years[yearIndex]+'-12-31'
            index = -1
            for j in range(10):#处理0值
                if j%2 == 0:
                    #虚晃一枪
                    tempDay = random.randint(int(years[yearIndex]),2019)
                    tempDay = str(tempDay)+'-12-31'
                    baidu_index = BaiduIndex(keywords, startDay, tempDay, value)
                    baidu_index.get_index(startDay)
                else:
                    #正式代码
                    baidu_index = BaiduIndex(keywords,startDay, endDay,value)
                    index = baidu_index.get_index(startDay)
                    #正式代码
                    if (index[0] != 0):
                        break


            temp = [];
            temp.append(index[0]);
            index = temp;
            index.append(keys)
            index.append(years[yearIndex])
            result.append(index)
            print(result)
        pd.DataFrame(result).to_csv('result.csv', encoding='gbk',mode='a')
        print("{0} in  is successfully saved" .format(years[yearIndex]))
        time.sleep(60)#避免反爬，暂停1min




