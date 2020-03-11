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
        'url':'https://www.harp.lg.jp/opendata/api/package_show?id=752c577e-0cbe-46e0-bebd-eb47b71b38bf',
        'type':'odp'
    },
    'patients_summary':{
        'url':'https://www.harp.lg.jp/opendata/api/package_show?id=752c577e-0cbe-46e0-bebd-eb47b71b38bf',
        'type':'odp'
    },
    'discharges_summary':{
        'url':'https://www.harp.lg.jp/opendata/api/package_show?id=752c577e-0cbe-46e0-bebd-eb47b71b38bf',
        'type':'odp'
    },
    'current_patients':{
        'url':'https://www.harp.lg.jp/opendata/api/package_show?id=752c577e-0cbe-46e0-bebd-eb47b71b38bf',
        'type':'odp'
    }
}

#ヘッダーにkeyがあればvalueに置き換えます
HEADER_TRANSLATIONS = {
    '小計':'subtotal',
    '日付':'date',
    'No':'no',
    '\ufeffNo':'no',#ODPのデータが綺麗になったら不要
    'リリース日':'date',
    '居住地':'place',
    '年代':'age',
    '性別':'sex',
    '患者数':'subtotal',
    '日陽性数':'subtotal',
    '日治療終了数':'subtotal'
}

#先にある順にデコードされます
CODECS = ['utf-8','cp932','shift_jis','euc_jp',
          'euc_jis_2004','euc_jisx0213',
          'iso2022_jp','iso2022_jp_1','iso2022_jp_2','iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext',
          'shift_jis_2004','shift_jisx0213',
          'utf_16','utf_16_be','utf_16_le','utf_7','utf_8_sig']