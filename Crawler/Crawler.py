import requests
import re
import xlwt
from bs4 import BeautifulSoup
list=['haitangqu','tainyaqu','xinbei','jiyangb']
wk = xlwt.Workbook()
sheet = wk.add_sheet("haidian")
row = 0
for i in list:
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39"}
    url = "https://www.anjuke.com/fangjia/nantong2022/{}/".format(i)
    r = requests.get(url,headers=headers)
    r.encoding="utf-8"
    # print(r.text)
    bs = BeautifulSoup(r.text,"html.parser")
    ul = bs.select('body > div.main-content > div.avger.clearfix > div.fjlist-wrap.clearfix > div:nth-child(1) > ul > li')

    sheet.write(row, 0, "时间")
    sheet.write(row, 1, "均价")
    sheet.write(row, 2, "环比")
    row+=1
    for item in ul:
        # print(item.text.split()[1])
        sheet.write(row,0,item.text.split()[0])
        sheet.write(row,1,item.text.split()[1])
        sheet.write(row,2,item.text.split()[2])
        row+=1
wk.save("a2.xls")

