import pandas as pd
import requests
import csv
import json


def gaode(addr):
    para = {
        'key': '3bb588306f1be9cfd10ebe502813041c',  # 高德地图开放平台申请的key
        'address': addr  # 传入地址参数
    }
    url = 'https://restapi.amap.com/v3/geocode/geo?'  # 高德地图API接口
    req = requests.get(url, para)
    req = req.json()
    # print('-' * 30)
    m = req['geocodes'][0]['location']
    print(m)
    return m


# gaode(addr="柏林寺西")

df2 = pd.read_excel('gz_school.xls')  # 读取地址数据
df2['经纬度'] = df2['address'].apply(gaode)  # 调用函数

df2.head()
df2.to_excel('result.xls', index=False)


