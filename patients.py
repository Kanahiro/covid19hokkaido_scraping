
import sys
import csv
import json
import re
import datetime
import urllib.request
from bs4 import BeautifulSoup

START_YEAR = 2020

class PatientsReader:
    def __init__(self, url='http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm'):
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
        parsed_date_str = self.parse_datetext(date_str)

        self.data = table_data
        self.date = parsed_date_str

    def make_patients_dict(self):
        patients = {
            'date':self.date,
            'data':[]
        }

        #patients data
        headers = self.data[0]
        maindatas = self.data[1:]
        patients_data = []

        #rewrite header 公表日 as リリース日
        for i in range(len(headers)):
            if headers[i] == '公表日':
                headers[i] = 'リリース日'
                break

        prev_month = 0 #to judge whether now is 2020 or more
        for data in maindatas:
            dic = {}
            for i in range(len(headers)):
                dic[headers[i]] = data[i]
                #translate MM/DD to ISO-8601 datetime
                if headers[i] == 'リリース日':
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
                    #rewrite 公表日 as リリース日
                    dic[headers[i]] = date_str

            patients_data.append(dic)

        patients['data'] = patients_data
        return patients

    def make_patients_summary_dict(self):
        patients = self.make_patients_dict()
        summary = self.calc_patients_summary(patients)
        patients_summary = {'data': summary, 'date': self.date}
        return patients_summary

    def make_json(self, url:str, filename:str):
        dicts = make_dicts(url)
        write_json(filename, dicts)

    def make_csv(self, url:str):
        dicts = make_dicts(url)
        for key in dicts:
            write_csv(key + '.csv', dicts[key]['data'])

    def write_csv(self, filepath:str, dicts:list):
        with open(filepath, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, dicts[0].keys())
            writer.writeheader()
            writer.writerows(dicts)

    #sample:最終更新日：2020年3月05日（木）
    def parse_datetext(self, datetext:str)->str:
        parsed_date = re.split('[^0-9]+', datetext)[1:4]
        year = int(parsed_date[0])
        month = int(parsed_date[1])
        day = int(parsed_date[2])
        date = datetime.datetime(year, month, day)
        date_str = date.isoformat()
        return date_str

    def calc_patients_summary(self, patients:dict)->list:
        summary = []

        start_day = patients['data'][0]['リリース日']
        start_datetime = datetime.datetime.fromisoformat(start_day)

        end_datetime = datetime.datetime.fromisoformat(patients['date'])
        while start_datetime <= end_datetime:
            day = {
                '日付':'',
                '小計':0
            }
            day['日付'] = start_datetime.isoformat()
            
            for p in patients['data']:
                if p['リリース日'] == day['日付']:
                    day['小計'] = day['小計'] + 1

            summary.append(day)
            start_datetime = start_datetime + datetime.timedelta(days=1)

        return summary


    def write_json(self, filepath:str, dic:dict):
        with open(filepath, 'w') as f:
            json.dump(dic, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    pr = PatientsReader()
    print(pr.make_patients_dict())
    print(pr.make_patients_summary_dict())
    #pr.make_csv(url='http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm')
    #pr.make_json(url='http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm', filename='data.json')