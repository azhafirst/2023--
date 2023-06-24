import requests
import re
import xlwt
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39"}
page=1
row=1
while page<150:
    r = requests.get("https://house-pricing.herokuapp.com/houses?_method=get&authenticity_token=5u1VoAa8fYU%2FoUiRFExjtVg16yw%2BRaQWcT2VoVt%2BzetEtnxsL1riXTAzKrbmRvup8goZC5H1FeoLUo8arlorVA%3D%3D&page="+str(page),headers=headers)
    r.encoding="utf-8"
    page+=1
    bs = BeautifulSoup(r.text, "html.parser")
    wk = xlwt.Workbook()
    sheet = wk.add_sheet("北京")

    sheet.write(0,0,"ID")
    # sheet.write(0,1,"小区名")
    # sheet.write(0,2,"建造时间")
    # sheet.write(0,3,"楼层")
    # sheet.write(0,4,"面积")
    # sheet.write(0,5,"房型")
    # sheet.write(0,6,"医院")
    # sheet.write(0,7,"公交")
    # sheet.write(0,8,"商场")
    # sheet.write(0,9,"地铁")
    # sheet.write(0,10,"学校")
    # sheet.write(0,11,"写字楼")
    # sheet.write(0,12,"均价")
    # row = 1
    trs = bs.select(r'#page-wrapper > div.panel.panel-default > div.panel-body > table > tbody > tr')

    for tr in trs:
        td = tr.select(r'td')
        sheet.write(row, 0, str(td[0].text))
        sheet.write(row, 1, str(td[1].text))
        sheet.write(row, 2, str(td[2].text))
        sheet.write(row, 3, str(td[3].text))
        sheet.write(row, 4, str(td[4].text))
        sheet.write(row, 5, str(td[5].text))
        sheet.write(row, 6, str(td[6].text))
        sheet.write(row, 7, str(td[7].text))
        sheet.write(row, 8, str(td[8].text))
        sheet.write(row, 9, str(td[9].text))
        sheet.write(row, 10, str(td[10].text))
        sheet.write(row, 11, str(td[11].text))
        sheet.write(row, 12, str(td[12].text))
        row+=1
wk.save("bjdata1.xls")