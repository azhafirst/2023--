import requests
import re
from bs4 import BeautifulSoup

root = r'https://zz.lianjia.com/ershoufang/'

districts = {}  # 郑州市地区名称对应 url
houses = []  # 房屋具体信息列表

session = requests.session()


def handle_single_page(single_page: BeautifulSoup(), house: {}) -> None:
    """
    抓取每一项具体房源信息
    :param single_page: 原始房源信息页面
    :param house: 已经填充了 ID 的 house 字典
    :return: None
    """
    overview = single_page.select('div[class="overview"]')[0]

    # 主要信息
    house["标题"] = single_page.select('div[class="title"] > h1')[0].string
    house["副标题"] = single_page.select('div[class="title"] > div')[0].string
    house["总价"] = overview.select('span[class="total"]')[0].string
    house["总价单位"] = overview.select('span[class="unit"] > span')[0].string
    house["均价"] = overview.select('div[class="unitPrice"]')[0].text
    house["小区名称"] = overview.select('div[class="communityName"] > a[target="_blank"]')[0].string
    house["所在区域"] = overview.select('div[class="areaName"] > span[class="info"]')[0].text.replace('\xa0', ' ')

    # 基本信息 -> 基本属性
    base = single_page.select('div[class="base"] > div[class="content"] > ul > li')
    for node in base:
        name, value = node.contents
        house[name.string] = value

    # 基本信息 -> 交易属性
    transaction = single_page.select('div[class="transaction"] > div[class="content"] > ul > li')
    for node in transaction:
        name, value = node.select('span')
        name, value = name.string, value.string.strip()
        house[name] = value


def handle_page(page: int, district_url: str) -> None:
    """
    逐个查询一页中的每一项房源信息
    :param district_url: 将要查询的地区 url
    :param page: 指定页数
    :return: None
    """
    global houses

    url = root + district_url + f'pg{page}/'
    listpage = BeautifulSoup(session.get(url).text, features='html.parser')

    single_page_urls = listpage.select('div[class="title"] > a')
    for j in single_page_urls:
        house = {}
        house_url = j.get('href')
        # 直接获取 url 中的 ID 作为 id
        house['ID'] = re.findall(root + r'(\d*).html', house_url)[0]

        # 获取某个房屋的具体信息
        single_page = BeautifulSoup(session.get(house_url).text, features='html.parser')

        # 获取房屋信息字典
        handle_single_page(single_page, house)

        houses.append(house)


def get_districts() -> None:
    """
    在链家网首页查找所有可用的地区
    :return: None
    """
    global districts

    main_page = BeautifulSoup(session.get(root).text, features='html.parser')
    districts_block = main_page.select('body > div:nth-child(12) > div > div.position > dl:nth-child(2) > dd > '
                                       'div:nth-child(1) > div > a')

    for j in districts_block:
        district_code = re.findall(r'/ershoufang/(\w+)/', j.get('href'))[0]
        district_name = re.findall(r'郑州([\u4e00-\u9fa5]+)在售二手房', j.get('title'))[0]
        districts[district_name] = district_code


def write_to_csv(path: str) -> None:
    """
    将房屋信息写入 csv 文件
    :param path: 目标 csv 文件的位置
    :return: None
    """
    global houses

    with open(path, 'a',encoding='utf-8') as f:
        for house in houses:
            for val in house.values():
                f.write(f"{val},")
            f.write('\n',)

    houses = []


def main() -> None:
    """
    主函数
    :return: None
    """
    get_districts()

    for district_name in districts.keys():
        for page in [1]:
            print(f'{district_name}\tpage: {page}')
            handle_page(page, f'{districts[district_name]}/')
            write_to_csv(r'D:\pycharm\PyCharm 2018.2.3\p2\venv\Include\d2.csv')

        print()


if __name__ == '__main__':
    main()