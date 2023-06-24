import xlwt  #向excel中写数据
import xlrd  #从excel中读取数据
import os
import math
#获取workbook对象

import pymysql
#1.添加数据

#1.和数据库建立连接
conn=pymysql.connect(
    host="localhost", #host name
    port=3306,
    db="houseprice",
    user="root",
    password="",
    charset='utf8'
)
#print(conn)
# 2.创建游标对象
cls=conn.cursor()
'''
#3.创建sql语句
sql="insert into myuser values(null,%s,%s)"
#4.执行
rows=cls.execute(sql,['张三','ROOT'])
print("影响的行数：",rows)
'''

#cls.execute("insert into 城市表 values(1,'深圳',null,70250)")

'''
sheet=wk3.sheet_by_index(8)
for i in range(1,sheet.nrows):
    #print(sheet.row_values(i)[1],str(int(sheet.row_values(i)[2].replace(',',''))))
    sql = "insert into 区域表 values(null,%s,null,%s,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null)"
    rows = cls.execute(sql, [str(sheet.row_values(i)[1]), str(int(sheet.row_values(i)[2]))])
    conn.commit()


min=10000
max=20000
sql="select 城市区域关系表.城市名,城市区域关系表.区域名,区域表.现房价 from 城市区域关系表,区域表 where 城市区域关系表.区域名=区域表.区域名 and 现房价>=%s and 现房价<=%s"
rows=cls.execute(sql,[str(min),str(max)])
result = cls.fetchall()
print(len(result))
print(result)
'''


'''
#通过名字获取sheet
for i in range(3,11):
    sheet=wk1.sheet_by_index(i)
    #sheet2=wk2.sheet_by_index(i)
    #sheet3=wk3.sheet_by_index(i)
    
    sql = "select 区域名 from 城市区域关系表 where 城市名=%s"  # uid>66
    cls.execute(sql,[citysheet.row_values(i)[1]])
    result = cls.fetchall()  # fetchall()则变为多条查询
    print(len(result))
    sqll="update 城市表 set 区域数=%s where 城市名=%s"
    rows=cls.execute(sqll,[str(len(result)),citysheet.row_values(i)[1]])
    for k in range(1, sheet.nrows):
    quname=sheet.row_values(k)[1]
    sql="insert into 城市区域关系表 values(null,%s,%s)"
    rows=cls.execute(sql,[citysheet.row_values(i+21)[1],sheet.row_values(k)[1]])
    
    #批量添加
    for k in range(1,sheet.nrows):
        sql="insert into 区域表 values(null,%s,null,%s,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null)"
        rows=cls.execute(sql,[str(sheet.row_values(k)[1]),str(sheet.row_values(k)[2].replace(',',''))])
    conn.commit()
    print(i)
'''

'''
for i in range(0,10):
    sheet=wk2.sheet_by_index(i)
    for k in range(1,sheet.nrows):
        sql="insert into 区域表 values(null,%s,null,%s,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null)"
        rows=cls.execute(sql,[str(sheet.row_values(k)[1]),str(sheet.row_values(k)[2].replace(',',''))])
    conn.commit()
    print(i)


for i in range(8,10):
    sheet=wk3.sheet_by_index(i)
    for k in range(1,sheet.nrows):
        sql="insert into 区域表 values(null,%s,null,%s,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null)"
        rows=cls.execute(sql,[str(sheet.row_values(k)[1]),str(sheet.row_values(k)[2].replace(',',''))])
    conn.commit()
    print(i)
'''

'''
for i in range(sheet.nrows):
    sql="insert into 北京房产表 values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    rows=cls.execute(sql,[sheet.row_values(i)[j] for j in range(1,24)])
    conn.commit()
'''
'''
#填充北京区域街道关系表
for i in range(sheet.nrows):
    q=str(sheet.row_values(i)[0]).split(' ')
    q[0]=q[0]+"区"
    sql1="select * from 北京区域街道关系表 where 区域名=%s and 街道名=%s"
    rows1=cls.execute(sql1,[q[0],q[1]])
    result = cls.fetchall()
    if len(result)==0:
        sql2 = "insert into 北京区域街道关系表 values(null,%s,%s)"
        rows2 = cls.execute(sql2, [q[0], q[1]])
        conn.commit()
'''

'''
sql="select 街道名 from 北京区域街道关系表"
rows=cls.execute(sql)
result = cls.fetchall()
for i in result:
    print(i)
    cls.execute("insert into 北京街道表 values(null,%s)",[i[0]])
    conn.commit()


#填充北京街道房产关系表
for i in range(sheet.nrows):
    q=str(sheet.row_values(i)[0]).split(' ')
    sql = "insert into 北京街道房产关系表 values(null,%s,%s)"
    cls.execute(sql,[q[1],sheet.row_values(i)[3]])
conn.commit()
'''
'''
files=os.listdir("D:\袁一楠\大三下\生产实习\paqushuju\data")
for file in files:
    wk = xlrd.open_workbook("D:\袁一楠\大三下\生产实习\paqushuju\data\\"+file)
    print(file)
    for i in range(wk.nsheets):
        sheet = wk.sheet_by_index(i)
        if sheet.nrows==7:
            quname=sheet.name+"区"
            sq="select * from 区域表 where 区域名= %s"
            cls.execute(sq,[quname])
            result=cls.fetchall()
            if len(result)!=0:
                sql="update 区域表 set 2022年01月=%s,2022年02月=%s,2022年03月=%s,2022年04月=%s,2022年05月=%s,2022年06月=%s where 区域名=%s"
                cls.execute(sql,[str(sheet.row_values(6)[1]).split("元")[0],str(sheet.row_values(5)[1]).split("元")[0],str(sheet.row_values(4)[1]).split("元")[0],
                                 str(sheet.row_values(3)[1]).split("元")[0],str(sheet.row_values(2)[1]).split("元")[0],str(sheet.row_values(1)[1]).split("元")[0],
                                 quname])
    conn.commit()
'''
'''
wk = xlrd.open_workbook("D:\袁一楠\大三下\生产实习\paqushuju\data\南京.xls")
for i in range(wk.nsheets):
    sheet = wk.sheet_by_index(i)
    if sheet.nrows==7:
        quname=sheet.name+"区"
        sq="select * from 区域表 where 区域名= %s"
        cls.execute(sq,[quname])
        result=cls.fetchall()
        if len(result)!=0:
            sql="update 区域表 set 2022年01月=%s,2022年02月=%s,2022年03月=%s,2022年04月=%s,2022年05月=%s,2022年06月=%s where 区域名=%s"
            cls.execute(sql,[str(sheet.row_values(6)[1]).split("元")[0],str(sheet.row_values(5)[1]).split("元")[0],str(sheet.row_values(4)[1]).split("元")[0],
                             str(sheet.row_values(3)[1]).split("元")[0],str(sheet.row_values(2)[1]).split("元")[0],str(sheet.row_values(1)[1]).split("元")[0],
                             quname])
    conn.commit()
'''
'''
wk = xlrd.open_workbook("D:\袁一楠\大三下\生产实习\paqushuju\北京.xls")
sheet = wk.sheet_by_index(0)
for i in range(1,sheet.nrows):
    print(i)
    z=str(sheet.row_values(i)[2]).split(',')
    sql="update 北京房产表 set 经度=%s,纬度=%s where 房产名称=%s"
    cls.execute(sql,[z[0],z[1],sheet.row_values(i)[1]])
    conn.commit()
'''
'''
wk = xlrd.open_workbook("D:\袁一楠\大三下\生产实习\paqushuju\\1.xls")
sheet = wk.sheet_by_index(0)
wk2=xlwt.Workbook()
s=wk2.add_sheet("1")
s.write(0,0,"酒店")
s.write(0,1,"医院")
s.write(0,2,"大学")
s.write(0,3,"中学")
s.write(0,4,"地铁站")
for i in range(1,sheet.nrows):
    z=str(sheet.row_values(i)[2]).split(',')
    jd,yy,dx,zx,dtz=0,0,0,0,0
    for j in range(1,wk.nsheets):
        sh = wk.sheet_by_index(j)
        for k in range(1,sh.nrows):
            y=str(sh.row_values(k)[1]).split(',')
            juli=math.sqrt(math.pow(float(z[0])-float(y[0]),2)+math.pow(float(z[1])-float(y[1]),2))
            juli=juli*111
            if juli <= 3 and j==1:
                jd=jd+1
            elif juli<=3 and j==2:
                yy=yy+1
            elif juli<=3 and j==5:
                dtz=dtz+1
            elif juli<=3 and j==3:
                dx=dx+1
            elif juli<=3 and j==4:
                zx=zx+1
    s.write(i,0,jd)
    s.write(i,1,yy)
    s.write(i,2,dx)
    s.write(i,3,zx)
    s.write(i,4,dtz)
    print(jd,yy,dx,zx,dtz)
wk2.save("2.xls")
'''
wk = xlrd.open_workbook("D:\生产实习\\1.xls")
sheet = wk.sheet_by_index(0)
for i in range(1, sheet.nrows):
    sql="update 北京房产表 set 酒店=%s,医院=%s,大学=%s,中学=%s,地铁站=%s where 房产名称=%s"
    cls.execute(sql, [sheet.row_values(i)[3], sheet.row_values(i)[4], sheet.row_values(i)[5],
                      sheet.row_values(i)[6], sheet.row_values(i)[7], sheet.row_values(i)[1]])
conn.commit()
#5.关闭
conn.close()

