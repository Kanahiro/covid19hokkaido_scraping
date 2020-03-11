import csv
import json
import datetime
import glob
import os
import urllib.request
from patients import PatientsReader

JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')

class CovidDataManager:
    def __init__(self):
        self.data = {
            'contacts':{},
            'querents':{},
            'patients':{},
            'patients_summary':{},
            'discharges':{},
            'discharges_summary':{},
            'inspections':{},
            'inspections_summary':{},
            'better_patients_summary':{},
            'last_update':datetime.datetime.now(JST).isoformat(),
            'main_summary':{}
        }

    def fetch_data(self):
        pr = PatientsReader()
        self.data['patients'] = pr.make_patients_dict()
        self.data['patients_summary'] = pr.make_patients_summary_dict()

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

    def import_csv_from_odp(self):
        responce = urllib.request.urlopen('https://www.harp.lg.jp/opendata/api/package_show?id=752c577e-0cbe-46e0-bebd-eb47b71b38bf')
        print(responce.getcode())
        if responce.getcode() == 200:
            loaded_json = json.loads(responce.read().decode('utf-8'))
            if loaded_json['success'] == True:
                resources = loaded_json['result']['resources']
                for resource in resources:
                    url = resource['download_url']
                    request_file = urllib.request.urlopen(url)
                    if request_file.getcode() == 200:
                        f = request_file.read().decode('utf-8')
                        print(resource['filename'])
                        filename = resource['filename'].replace('.csv', '')
                        last_modified_time = resource['updated']
                        datas = []
                        rows = [row for row in csv.reader(f.splitlines())]
                        header = rows[0]
                        for i in range(len(header)):
                            header[i] = header[i].replace('\ufeff', '')

                        maindatas = rows[1:]
                        for d in maindatas:
                            data = {}
                            for i in range(len(header)):
                                if filename == "current_patients":
                                    if header[i] == '患者数':
                                        data['subtotal'] = int(d[i])
                                    if header[i] == '日付':
                                        data['date'] = d[i]

                                elif filename == "patients":
                                    if header[i] == 'リリース日':
                                        data['date'] = d[i]
                                    if header[i] == 'No':
                                        data['no'] = d[i]
                                    if header[i] == '年代':
                                        data['age'] = d[i]
                                    if header[i] == '性別':
                                        data['sex'] = d[i]
                                    if header[i] == '居住地':
                                        data['place'] = d[i]
                                    if header[i] == '周囲の状況':
                                        data['other_patient'] = d[i]
                                    if header[i] == '濃厚接触者の状況':
                                        data['contact_person'] = d[i]
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
    dm.import_csv_from_odp()
    dm.import_csv_from_sdp_contacts()
    dm.import_csv_from_sdp_querents()
    for key in dm.data:
        dm.export_json_from_name(key)