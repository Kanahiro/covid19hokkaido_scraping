
import sys
import csv
import json
import urllib.request
from bs4 import BeautifulSoup

def make_json(url:str, filepath:str):
    datas = get_datas(url)
    table = datas['table']
    date = datas['date']
    dicts = to_dicts(table, date)
    write_json(filepath, dicts)

def make_csv(url:str, filepath:str):
    datas = get_datas(url)
    table = datas['table']
    write_csv(filepath, table)

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

def write_csv(filepath:str, rows:list):
    with open(filepath, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)

def to_dicts(datas:list, date:str)->list:
    import re

    data_dict = {
        'patients':{
            'date':'',
            'data':[]
        }
    }

    #datetext parsing
    parsed_date = re.split('[^0-9]+', date)[1:4]
    year = parsed_date[0]
    month = parsed_date[1]
    day = parsed_date[2]
    date_str = year + '/' + month + '/' + day
    data_dict['patients']['date'] = date_str

    #patients data
    headers = datas[0]
    maindatas = datas[1:]
    patients_data = []
    for data in maindatas:
        dic = {}
        for i in range(len(headers)):
            dic[headers[i]] = data[i]
        patients_data.append(dic)
    data_dict['patients']['data'] = patients_data
    return data_dict

def write_json(filepath:str, dic:dict):
    with open(filepath, 'w') as f:
        json.dump(dic, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    make_csv(url='http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm', filepath='covid19hokkaido.csv')
    make_json(url='http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm', filepath='data.json')