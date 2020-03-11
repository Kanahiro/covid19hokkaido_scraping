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
    }
}

HEADER_TRANSLATIONS = {
    '小計':'subtotal',
    '日付':'date',
    'No':'no',
    '\ufeffNo':'no',#ODPのデータが綺麗になったら不要
    'リリース日':'date',
    '居住地':'place',
    '年代':'age',
    '性別':'sex',
}