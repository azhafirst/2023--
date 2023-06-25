import pickle

from flask import Flask, render_template, request, jsonify
import pymysql
import json
import pymysql
from sklearn import linear_model
import numpy as np
"""
static: CSS文件,JS文件,图片
templates:html网页
"""
app = Flask(__name__)

@app.route("/userLogin")
def userLogin():
    return render_template("index.html")

@app.route("/")
def ZY():
    return render_template("SY.html")

@app.route("/Login")
def Login():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        db="houseprice",
        user="root",
        password="",
        charset="utf8"
    )
    uname = request.args.get("uname")
    upwd = request.args.get("upwd")
    cls = conn.cursor()
    sql="select 用户名,密码 from 用户表 where 用户名='"+uname+"'"
    row = cls.execute(sql)
    result = cls.fetchone()
    if result[1] == upwd:
        return render_template("MULU.html")
    else:
        return render_template("index.html")


@app.route("/Uregister")
def Uregister():
    return render_template("UserRegister.html")

@app.route("/search")
def search():
    city = request.args.get("city")
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        db="houseprice",
        user="root",
        password="",
        charset="utf8"
    )
    regions=[]
    prices=[]
    cls = conn.cursor()
    sql = "select 区域表.区域名,现房价 from 城市区域关系表,区域表 where 城市区域关系表.区域名=区域表.区域名 and 城市名=%s"
    cls.execute(sql, [city])
    result = cls.fetchall()
    print(result)
    for i in result:
        regions.append(i[0][0:2])
        prices.append(i[1])
    print(regions)
    print(prices)
    conn.commit()
    return render_template("text.html", region=regions, price=prices)

@app.route("/SearchText")
def SearchText():
    regions=[' ']
    return render_template("text.html",region=regions)

@app.route("/UserRegister")
def UserRegister():
    #获取前端的数据
    #获取用户名
    name = request.args.get("uname")
    pwd = request.args.get("upwd")
    print("姓名：",name,"密码:",pwd)
    #到数据库中添加数据
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        db="houseprice",
        user="root",
        password="",
        charset="utf8"
    )
    cls =conn.cursor()
    sql="insert into 用户表 values(null,%s,%s)"
    rows = cls.execute(sql,[name,pwd])
    print(rows)
    conn.commit()
    if rows>=1:  #添加成功
        #从数据库中查询用户信息，显示到前端
        conn.close()
        return render_template("index.html")
    else:
        return render_template("UserRegister.html")

@app.route("/echarts")
def echarts():
    return  render_template("echarts.html")

@app.route("/showEcharts")
def showEcharts():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        db="houseprice",
        user="root",
        password="",
        charset="utf8"
    )
    cls = conn.cursor()
    sql="select * from houses where id <15"
    cls.execute(sql)
    result = cls.fetchall()
    print(result)
    dict1={}
    list1=[]
    for i in result:
         list1.append(i[3])
    dict1["data"]=list1  #{data: [1,3,4,5,6,7...]}
    print(dict1)
    return  json.dumps(dict1)

@app.route("/searchP")
def searchP():
    return render_template("SearchByPrice.html")

@app.route("/searchPrice")
def searchPrice():
    minprice=request.args.get("minprice")
    maxprice = request.args.get("maxprice")
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        db="houseprice",
        user="root",
        password="",
        charset="utf8"
    )
    cls = conn.cursor()
    sql = "select 城市区域关系表.城市名,城市区域关系表.区域名,区域表.现房价 from 城市区域关系表,区域表 where 城市区域关系表.区域名=区域表.区域名 and 现房价>=%s and 现房价<=%s"
    rows = cls.execute(sql, [str(minprice), str(maxprice)])
    result = cls.fetchall()
    print(len(result))
    print(result)
    dict1 = {}
    list1 = []
    for i in result:
        list1.append(i)
    dict1["data"] = list1  # {data: [1,3,4,5,6,7...]}
    print(dict1)


    return render_template("SearchByPrice.html", content=result,labels=['城市','城区','平均房价'])


@app.route("/AJAXtest")
def AJAXtest():
    return render_template("AJAXtest.html")

@app.route('/testGet',methods=['GET'])
def testGet():
    data = request.args.get('name')
    dataP = request.args.get('dataP')
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        db="houseprice",
        user="root",
        password="",
        charset="utf8"
    )
    cls = conn.cursor()
    sql = "select 区域表.区域名,现房价 from 城市区域关系表,区域表 where 城市区域关系表.区域名=区域表.区域名 and 城市名='北京'"
    cls.execute(sql)
    result = cls.fetchall()
    print(data)
    return jsonify({'status':True,'dataP': result})

@app.route('/MULU')
def MULU():
    return render_template("MULU.html")

@app.route('/ZX')
def ZX():
    return render_template("ZouXiang.html",data = [],region = [])

@app.route('/searchZX')
def searchZX():
    datas=[]
    regionL = request.args.get("region")
    region = regionL.split(" ")
    print(region)
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        db="houseprice",
        user="root",
        password="",
        charset="utf8"
    )
    print(region)
    cls = conn.cursor()
    str1 = " or 区域名=%s"
    sql = "select * from 区域表 where 区域名=%s"
    for i in range(len(region)-1):
        sql = sql + str1


    rows = cls.execute(sql, region)
    result = cls.fetchall()
    print(result)
    if rows >=1:
        for lists in result:
            print(lists)
            dict1={}
            dict1['name']=lists[1]
            if rows == 1:
                dict1['type'] = "bar"
            else:
                dict1['type']="line"
            dict1['data']=list(lists[2:9])
            temp1 = predict(lists[3:9])
            print(temp1)
            tempList = list(lists[3:9])
            tempList.append(temp1)
            print("tempList",tempList[1:7])
            dict1['data'].append(temp1)
            temp2 = predict(tempList[1:7])
            dict1['data'].append(temp2)
            datas.append(dict1)
            print(dict1)
            print(region)
        print(datas)
        return render_template("ZouXiang.html", data = datas , region= region)
    else:
        return render_template("ZouXiang.html", data = datas, region = "无")

def predict(a):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        db="houseprice",
        user="root",
        password="",
        charset="utf8"
    )
    cls = conn.cursor()
    sql = "select * from 区域表 where `2022年01月` is not NULL "
    rows = cls.execute(sql)
    result = cls.fetchall()
    datas = []
    for i in result:
        datas.append(list(i[2:9]))
 #   print(rows, datas)
    xt = []
    yt = []
    for i in datas:
        xt.append(i[1:7])
        yt.append(i[0])

    x = np.array(xt)
    y = np.array(yt)
 #   print(x, y)
    # 定义训练样本

    # 线性回归对象
    reg = linear_model.LinearRegression()
    # 训练
    reg.fit(x, y)

    print('截距', reg.intercept_)
    print('回归参数', reg.coef_)
    # 预测
    res = reg.predict([a])
    print('预测结果', int(res[0]))
    return int(res[0])

@app.route('/searchByIncome')
def searchByIncome():
    return render_template("searchByIncome.html")

@app.route('/searchByIC')
def searchByIC():
    income = int(request.args.get("input"))
    print(type(income))
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        db="houseprice",
        user="root",
        password="",
        charset="utf8"
    )
    incomeAll =int(income * 12 / 10000)
    HousePrice = incomeAll * 6
    cls = conn.cursor()
    sql = "select 总价格,单价,建筑面积,房产名称,详细说明,酒店,医院,大学,中学,地铁站 from 北京房产表 where  总价格 <= %s"
    rows = cls.execute(sql, [HousePrice])
    result = cls.fetchall()
    print(rows,result)

    if rows >= 0:
        return render_template("searchByIncome.html", content=result, labels=['总房价','单位价格','面积','房产名','详细介绍','酒店','医院','大学','中学','地铁站'])
    else:
        return render_template("searchByIncome.html")

@app.route("/RLT")
def RLT():
    return render_template("RLT.html")

if __name__ == '__main__':
    app.run()
