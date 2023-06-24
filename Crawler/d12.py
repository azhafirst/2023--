import requests
import re
import xlwt
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39"}
r = requests.get("http://sz.cityhouse.cn/market/BA/",headers=headers)
r.encoding = "utf-8"

bs = BeautifulSoup(r.text, "html.parser")
wk = xlwt.Workbook()
sheet = wk.add_sheet("宝安区")
sheet.write(0, 0, "排名")
sheet.write(0, 1, "区域")
sheet.write(0, 2, "平均房价")
sheet.write(0, 3, "环比上月")
row = 1
trs = bs.select(r'#halist > tbody > tr')

for tr in trs:
    td = tr.select(r'td')
    sheet.write(row,0,str(td[0].text))
    sheet.write(row, 1, str(td[1].text))
    sheet.write(row, 2, str(td[2].text))
    sheet.write(row, 3, str(td[3].text))
    row = row + 1
wk.save("szdata.xls")


