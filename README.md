![Python application](https://github.com/codeforsapporo/covid19hokkaido_scraping/workflows/Python%20application/badge.svg)

## What is this
北海道の新型コロナウイルス情報を集め、jsonやcsvとして出力するPythonスクリプトです

## Specification
- main.pyを実行すると、①settings.pyのREMOTE_SOURCESに基づき外部データを取得し、②importフォルダ内のcsvを読み込んで、データの数だけjsonファイルを出力します
- jsonの出力前に、データのカラム名は[北海道 新型コロナウイルスまとめサイト](https://github.com/codeforsapporo/covid19)に準拠するよう変換されます(settings.pyのHEADER_TRANSLATIONSに基づきます)
- settings.pyとimportフォルダ内に、同じkeyがある場合、importフォルダが優先されます

## 現在実装されているデータ
| データ |  key  |  source  | url  |
| ---- | ---- | ---- | ---- |
|  陽性患者の属性  |  patients  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369.html  |
|  陽性患者数（日別）  |  patients_summary  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369.html  |
|  日別患者増減数  |  current_patients  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369.html  |
|  治療修了者数  |  discharges_summary  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369.html  |
|  日別検査数  |  inspections  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369.html  |
|  日別窓口相談件数（札幌市保健所）  |  contacts  | DATA SMART CITY SAPPORO |  https://ckan.pf-sapporo.jp/dataset/covid_19_soudan  |
|  日別電話相談件数 （札幌市保健所） |  querents  | DATA SMART CITY SAPPORO |  https://ckan.pf-sapporo.jp/dataset/covid_19_soudan  |

## Scheduling
GitHub Actionsにより15分に一度、main.pyを実行してjson類をgh-pagesブランチに書き出します

## 外部からのアクセス
gh-pagesブランチにあるjsonデータに直接アクセスしてデータを読み出す事が出来ます。
sample: https://raw.githubusercontent.com/codeforsapporo/covid19hokkaido_scraping/gh-pages/patients.json
