import pandas
import requests
from bs4 import BeautifulSoup as BS

def get_nps_data():
    x = pandas.read_excel('excel_files/nps_2018.xlsx', sheet_name='국내주식 종목별 투자 현황(2018년 말)')
    data = {}
    data['번호'] = list(x['번호'])[0:199]
    data['종목명'] = list(x['종목명'])[0:199]
    data['평가액'] = list(x['평가액(억원)'])[0:199]
    data['자산군 내 비중'] = list(x['자산군 내 비중'])[0:199]
    data['지분율'] = list(x['지분율(%)'])[0:199]

    return data

'''
for i in data:
    vars()["data%d" % i] = []
    print(data[i])
    for j in i:
        vars()["data%d" % i].append
'''


def get_code():
    x = pandas.read_excel('excel_files/code_name_shares_cap.xlsx', sheet_name='Sheet1')
    data = {}
    data['name'] = list(x['종목명'])
    data['code'] = list(x['종목코드'])
    data['value'] = list(x['상장시가총액(원)'])
    data_list = []
    data_dict = {}
    for i in range(len(data['name'])):
        data_list.append([data['name'][i], data['code'][i], data['value'][i]])
        data_dict['%s'%data['name'][i]] = [data['code'][i], data['value'][i]]

    return data_dict


def get_real_time(code):
    response = requests.get('https://finance.naver.com/item/main.nhn?code=%s' % code)
    html = response.text
    soup = BS(html, 'html.parser')
    #print(soup)
    for tag in soup.select('div[class=rate_info]'):
        x = tag.text.split()[2].split(',')
        if tag.text.split()[2] == '오늘의시세':
            x = tag.text.split()[3].split(',')
        y = ''
        for i in x:
            y += i
        price = y
    for tag in soup.select('#tab_con1 > div.first > table '):

        x = tag.text.split()[9].split(',')
        if x == ['액면가l매매단위']:
            x = tag.text.split()[8].split(',')
        y = ''
        for i in x:
            y += i
        stock = y
    return [int(price), int(stock)]


def get_past_time(code):
    response = requests.get('https://finance.naver.com/item/sise_day.nhn?code=%s&page=17' % code)
    html = response.text
    soup = BS(html, 'html.parser')
    #print(soup)
    for tag in soup.select('body > table.type2'):
        x = tag.text.split()[8].split(',')
        y = ''
        for i in x:
            y += i
        price = y
    return int(price)


get_past_time('215600')