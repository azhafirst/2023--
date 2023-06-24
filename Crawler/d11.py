import requests
import re
import xlwt
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44"}

r = requests.get("https://ditu.amap.com/search?query=%E9%85%92%E5%BA%97&city=110000&geoobj=116.232292%7C39.771312%7C116.802208%7C40.052558&_src=around&zoom=11",headers=headers)
r.encoding = "utf-8"
# print(r.text)
bs = BeautifulSoup(r.text, "html.parser")
ul = bs.select('body > div.main-content > div.avger.clearfix > div.fjlist-wrap.clearfix > div:nth-child(1) > ul > li')

wk = xlwt.Workbook()
sheet = wk.add_sheet("haidian")
sheet.write(0, 0, "时间")
sheet.write(0, 1, "均价")
sheet.write(0, 2, "环比")
row = 1
for item in ul:
    # print(item.text.split()[1])
    sheet.write(row, 0, item.text.split()[0])
    sheet.write(row, 1, item.text.split()[1])
    sheet.write(row, 2, item.text.split()[2])
    row = row + 1
wk.save("a4.xls")
