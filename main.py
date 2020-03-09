import csv
import json
import datetime
import glob
import os
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

            with open('data/' + key + '.csv', 'w', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(csv_rows)

    def export_json(self, filepath='data/data.json'):
        with open(filepath, 'w') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def import_csv(self):
        csvfiles = glob.glob('./import/*.csv')
        for csvfile in csvfiles:
            filename = os.path.splitext(os.path.basename(csvfile))[0]
            last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(csvfile), JST).isoformat()
            datas = []
            with open(csvfile) as f:
                rows = [row for row in csv.reader(f)]
                header = rows[0]
                maindatas = rows[1:]
                for d in maindatas:
                    data = {}
                    for i in range(len(header)):
                        data[header[i]] = d[i]
                        if header[i] == '小計':
                            data[header[i]] = int(d[i])
                    datas.append(data)

            self.data[filename] = {
                'data':datas,
                'date':last_modified_time
            }

if __name__ == "__main__":
    dm = CovidDataManager()
    dm.fetch_data()
    dm.import_csv()
    dm.export_csv()
    dm.export_json()