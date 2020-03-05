
import sys
import csv
import json
import re
import datetime
import urllib.request
from bs4 import BeautifulSoup

START_YEAR = 2020

HEADER_PAIRS = {

}

def make_json(url:str, filepath:str):
    datas = get_datas(url)
    table = datas['table']
    date = datas['date']
    dicts = to_dicts(table, date)
    write_json(filepath, dicts)

def make_csv(url:str, filepath:str):
    datas = get_datas(url)
    table = datas['table']
    date = datas['date']
    dicts = to_dicts(table, date)['patients']['data']
    write_csv(filepath, dicts)

def get_datas(url:str)->dict:
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('Referer', 'http://localhost'),
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36 Edg/79.0.309.65'),
    ]

    html = opener.open(url)
    bs = BeautifulSoup(html, 'html.parser')

    table = bs.findAll('table')[0]
    trs = table.findAll('tr')

    table_data = []
    for i in range(len(trs)):
        cells = trs[i].findAll(['td', 'th'])
        row = []
        for cell in cells:
            cell_str = cell.get_text()
            #header cleaning
            if i == 0:
                cell_str = cell_str.replace(' ', '').replace(' ','')
            row.append(cell_str)
        table_data.append(row)

    date_str = bs.find(id='last_updated').get_text()

    datas = {
        'table': table_data,
        'date': date_str
    }

    return datas

def write_csv(filepath:str, dicts:list):
    with open(filepath, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, dicts[0].keys())
        writer.writeheader()
        writer.writerows(dicts)

def to_dicts(datas:list, date:str)->list:
    data_dict = {
        'patients':{
            'date':'',
            'data':[]
        }
    }

    #datetext parsing
    parsed_date = re.split('[^0-9]+', date)[1:4]
    year = int(parsed_date[0])
    month = int(parsed_date[1])
    day = int(parsed_date[2])
    date = datetime.datetime(year, month, day)
    date_str = date.isoformat()
    data_dict['patients']['date'] = date_str

    #patients data
    headers = datas[0]
    maindatas = datas[1:]
    patients_data = []

    prev_month = 0 #to judge whether now is 2020 or more
    for data in maindatas:
        dic = {}
        for i in range(len(headers)):
            dic[headers[i]] = data[i]
            #translate MM/DD to ISO-8601 datetime
            if headers[i] == '公表日':
                md = data[i].split('/')
                year = START_YEAR
                month = int(md[0])
                day = int(md[1])

                #2021 or more
                if month < prev_month:
                    year = START_YEAR + 1
                
                date = datetime.datetime(year, month, day)
                date_str = date.isoformat()
                prev_month = month
                dic[headers[i]] = date_str

        patients_data.append(dic)

    data_dict['patients']['data'] = patients_data
    return data_dict

def write_json(filepath:str, dic:dict):
    with open(filepath, 'w') as f:
        json.dump(dic, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    make_csv(url='http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm', filepath='covid19hokkaido.csv')
    make_json(url='http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm', filepath='data.json')