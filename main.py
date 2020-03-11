import csv
import json
import datetime
import glob
import os
import urllib.request

from patients import PatientsReader
from . import settings

JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
REMOTE_SOURCES = settings.REMOTE_SOURCES

class CovidDataManager:
    def __init__(self):
        self.data = {
            'last_update':datetime.datetime.now(JST).isoformat(),
        }

    def fetch_data(self):
        pr = PatientsReader()
        self.data['patients'] = pr.make_patients_dict()
        self.data['patients_summary'] = pr.make_patients_summary_dict()

    def fetch_datas(self):
        for key in REMOTE_SOURCES:
            self.fetch_data_of(key)

    def fetch_data_of(self, key):
        datatype = REMOTE_SOURCES[key]['type']
        data = {}
        if datatype == 'odp':
            
        elif datatype == 'csv':
        
        self[key] = data

    def export_csv(self):
        for key in self.data:
            if key == 'last_update' or key == 'main_summary':
                continue

            datas = self.data[key]
            if datas == {}:
                continue
            
            maindatas = datas['data']
            header = list(maindatas[0].keys())
            csv_rows = [ header ]
            for d in maindatas:
                csv_rows.append( list(d.values()) )

            with open('data/' + key + '.csv', 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(csv_rows)

    def export_json(self, filepath='data/data.json'):
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def export_json_from_name(self, key):
        with open('data/' + key + '.json', 'w', encoding='utf-8') as f:
            json.dump(self.data[key], f, indent=4, ensure_ascii=False)

    def import_csv(self):
        csvfiles = glob.glob('./import/*.csv')
        for csvfile in csvfiles:
            filename = os.path.splitext(os.path.basename(csvfile))[0]
            last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(csvfile), JST).isoformat()
            datas = []
            with open(csvfile, encoding='utf-8') as f:
                rows = [row for row in csv.reader(f)]
                header = rows[0]
                maindatas = rows[1:]
                for d in maindatas:
                    data = {}
                    for i in range(len(header)):
                        if filename == "current_patients":
                            if i <= 1:
                                if header[i] == '患者数':
                                    data['subtotal'] = int(d[i])
                                if header[i] == '日付':
                                    data['date'] = d[i]
                        else:
                            if header[i] == '小計':
                                data['subtotal'] = int(d[i])
                            if header[i] == '日付':
                                data['date'] = d[i]
                    datas.append(data)

            self.data[filename] = {
                'data':datas,
                'last_update':last_modified_time
            }

    def import_csv_from_odp(self, odp_url='https://www.harp.lg.jp/opendata/api/package_show?id=752c577e-0cbe-46e0-bebd-eb47b71b38bf'):
        responce = urllib.request.urlopen(odp_url)

        status_code = responce.getcode()
        if not status_code == 200:
            print(status_code, 'error occured')
            return

        loaded_json = json.loads(responce.read().decode('utf-8'))
        if not loaded_json['success']:
            print('get json error')
            return

        resources = loaded_json['result']['resources']
        for resource in resources:
            url = resource['download_url']
            request_file = urllib.request.urlopen(url)
            if request_file.getcode() == 200:
                f = request_file.read().decode('utf-8')
                filename = resource['filename'].rstrip('.csv')
                last_modified_time = resource['updated']
                datas = []
                rows = [row for row in csv.reader(f.splitlines())]
                header = rows[0]
                maindatas = rows[1:]
                for d in maindatas:
                    data = {}
                    for i in range(len(header)):
                        if filename == "current_patients":
                            if i <= 1:
                                if header[i] == '患者数':
                                    data['subtotal'] = int(d[i])
                                if header[i] == '日付':
                                    data['date'] = d[i]
                        else:
                            if header[i] == '小計':
                                data['subtotal'] = int(d[i])
                            if header[i] == '日付':
                                data['date'] = d[i]
                    datas.append(data)

                self.data[filename] = {
                    'data':datas,
                    'last_update':last_modified_time
                }

    def import_csv_from(self, url):
        request_file = urllib.request.urlopen(url)
        if not request_file.getcode() == 200:
            return
        
        f = request_file.read().decode('utf-8')
        filename = os.path.splitext(os.path.basename(csvfile))[0]
        datas = []
        rows = [row for row in csv.reader(f.splitlines())]
        header = rows[0]
        maindatas = rows[1:]
        for d in maindatas:
            data = {}
            for i in range(len(header)):
                if header[i] == '小計':
                    data['subtotal'] = int(d[i])
                if header[i] == '日付':
                    data['date'] = d[i]
            datas.append(data)

        self.data[filename] = {
            'data': datas,
            'last_update': datetime.datetime.now(JST).isoformat()
        }

    def import_csv_from_sdp_contacts(self):
        request_file = urllib.request.urlopen('https://ckan.pf-sapporo.jp/dataset/f6338cc2-dd6b-43b6-98a3-cd80b05b6a36/resource/e9e6f062-cafd-4aea-992f-039e2e26f4ac/download/contacts.csv')
        if request_file.getcode() == 200:
            f = request_file.read().decode('utf-8')
            filename = 'contacts'
            datas = []
            rows = [row for row in csv.reader(f.splitlines())]
            header = rows[0]
            maindatas = rows[1:]
            for d in maindatas:
                data = {}
                for i in range(len(header)):
                    if header[i] == '小計':
                        data['subtotal'] = int(d[i])
                    if header[i] == '日付':
                        data['date'] = d[i]
                datas.append(data)

            self.data[filename] = {
                'data': datas,
                'last_update': datetime.datetime.now(JST).isoformat()
            }

    def import_csv_from_sdp_querents(self):
        request_file = urllib.request.urlopen('https://ckan.pf-sapporo.jp/dataset/f6338cc2-dd6b-43b6-98a3-cd80b05b6a36/resource/a89ba566-93d1-416a-a269-e0ba48a06636/download/querents.csv')
        if request_file.getcode() == 200:
            f = request_file.read().decode('utf-8')
            filename = 'querents'
            datas = []
            rows = [row for row in csv.reader(f.splitlines())]
            header = rows[0]
            maindatas = rows[1:]
            for d in maindatas:
                data = {}
                for i in range(len(header)):
                    if header[i] == '小計':
                        data['subtotal'] = int(d[i])
                    if header[i] == '日付':
                        data['date'] = d[i]
                datas.append(data)

            self.data[filename] = {
                'data': datas,
                'last_update': datetime.datetime.now(JST).isoformat()
            }

if __name__ == "__main__":
    dm = CovidDataManager()
    dm.fetch_data()
    dm.import_csv()
    dm.import_csv_from_sdp_contacts()
    dm.import_csv_from_sdp_querents()
    for key in dm.data:
        dm.export_json_from_name(key)