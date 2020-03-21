![Python application](https://github.com/codeforsapporo/covid19hokkaido_scraping/workflows/Python%20application/badge.svg)

## What is this
北海道の新型コロナウイルス情報を集め、jsonやcsvとして出力するPythonスクリプトです

## Specification
- main.pyを実行すると、①settings.pyのREMOTE_SOURCESに基づき外部データを取得し、②①のデータを集計してmain_summaryを生成し、③importフォルダ内のcsvを読み込んで、それら全てのデータのjsonファイルを出力します
- jsonの出力前に、schemas.pyのスキーマ定義に基づきデータがバリデーションされます（異常が発生する場合jsonは出力されません）
- settings.pyとimportフォルダ内に同じkeyがある場合、importフォルダが優先されます

## 現在実装されているデータ
| データ |  key  |  source  | url  |
| ---- | ---- | ---- | ---- |
|  最終更新日時  |  last_update  | - |  スクリプト実行時点のdatetime  |
|  検査陽性者の状況  |  main_summary  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv を集計|
|  陽性患者の属性  |  patients  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2828/patients.csv |
|  陽性患者数（日別）  |  patients_summary  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv を集計|
|  日別患者増減数  |  current_patients  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv を集計|
|  治療修了者数  |  discharges_summary  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv を集計|
|  日別検査数  |  inspections  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv を集計|
|  日別窓口相談件数（札幌市保健所）  |  contacts  | DATA SMART CITY SAPPORO |  https://ckan.pf-sapporo.jp/dataset/f6338cc2-dd6b-43b6-98a3-cd80b05b6a36/resource/e9e6f062-cafd-4aea-992f-039e2e26f4ac/download/contacts.csv  |
|  日別電話相談件数 （札幌市保健所） |  querents  | DATA SMART CITY SAPPORO |  https://ckan.pf-sapporo.jp/dataset/f6338cc2-dd6b-43b6-98a3-cd80b05b6a36/resource/a89ba566-93d1-416a-a269-e0ba48a06636/download/querents.csv  |

## Scheduling
GitHub Actionsにより1時間に一度、main.pyを実行してjson類をgh-pagesブランチに書き出します

## 外部からのアクセス
gh-pagesブランチにあるjsonデータに直接アクセスしてデータを読み出す事が出来ます。
sample: https://raw.githubusercontent.com/codeforsapporo/covid19hokkaido_scraping/gh-pages/patients.json