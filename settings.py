#外部リソース定義
REMOTE_SOURCES = {
    'contacts':{
        'url':'https://ckan.pf-sapporo.jp/dataset/f6338cc2-dd6b-43b6-98a3-cd80b05b6a36/resource/e9e6f062-cafd-4aea-992f-039e2e26f4ac/download/contacts.csv',
        'type':'csv'
    },
    'querents':{
        'url':'https://ckan.pf-sapporo.jp/dataset/f6338cc2-dd6b-43b6-98a3-cd80b05b6a36/resource/a89ba566-93d1-416a-a269-e0ba48a06636/download/querents.csv',
        'type':'csv'
    },
    'patients':{
        'url':'https://www.harp.lg.jp/opendata/dataset/1369/resource/2828/patients.csv',
        'type':'csv'
    },
    'patients_summary':{
        'url':'https://www.harp.lg.jp/opendata/dataset/1369/resource/2829/patients_summary.csv',
        'type':'csv'
    },
    'discharges_summary':{
        'url':'https://www.harp.lg.jp/opendata/dataset/1369/resource/2833/discharges_summary.csv',
        'type':'csv'
    },
    'current_patients':{
        'url':'https://www.harp.lg.jp/opendata/dataset/1369/resource/2832/current_patients.csv',
        'type':'csv'
    },
    'inspections':{
        'url':'https://www.harp.lg.jp/opendata/dataset/1369/resource/2837/inspections.csv',
        'type':'csv'
    }
}

#ヘッダーにkeyがあればvalueに置き換えます
HEADER_TRANSLATIONS = {
}

#先にある順にデコードされます
CODECS = ['utf-8','cp932','shift_jis','euc_jp',
          'euc_jis_2004','euc_jisx0213',
          'iso2022_jp','iso2022_jp_1','iso2022_jp_2','iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext',
          'shift_jis_2004','shift_jisx0213',
          'utf_16','utf_16_be','utf_16_le','utf_7','utf_8_sig']