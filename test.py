# import xlwt
#
# wk = xlwt.Workbook()
# sheet = wk.add_sheet("haidian")
# sheet.write(0, 0, "时间")
# sheet.write(0, 1, "均价")
# sheet.write(0, 2, "环比")
# for i in range(1,100):
#     sheet.write(i,0,1000+i)
#     sheet.write(i,1,"asd")
#     sheet.write(i,2,"asds")
# wk.save("11.xlsx")
import pymysql
# 1.添加数据

# 1.和数据库建立连接
conn = pymysql.connect(
    host="localhost",
    port=3306,
    db="test",
    user="root",
    password="",
    charset='utf8'
)
print("good")
cls = conn.cursor()
sql="insert into myuser values (1,'asda','asd')"
cls.execute(sql)
conn.commit()
conn.close()
