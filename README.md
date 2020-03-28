![Python application](https://github.com/codeforsapporo/covid19hokkaido_scraping/workflows/Python%20application/badge.svg)

## What is this
北海道の新型コロナウイルス情報を集め、jsonやcsvとして出力するPythonスクリプトです

## Specification
#### main.py
- main.pyを実行すると、①settings.pyのREMOTE_SOURCESに基づき外部データを取得し、②①のデータを集計してmain_summaryを生成し、③importフォルダ内のcsvを読み込んで、それら全てのデータのjsonファイルを出力します
- jsonの出力前に、schemas.pyのスキーマ定義に基づきデータがバリデーションされます（データに異常があった場合jsonは出力されません）
- settings.pyとimportフォルダ内に同じkeyがある場合、importフォルダが優先されます
- このスクリプトでは、1つのCSVが1つのJSONに対応します（last_updateをのぞく）

#### covid19_data.py
- ODPのcovid19_data.csvを集計して、5つのjsonファイルを生成します（以下の対応表のとおり）


## 出力されるデータ
| データ |  key  |  source  | note  |
| ---- | ---- | ---- | ---- |
|  最終更新日時  |  last_update  | スクリプト実行時点のdatetime |  main.pyで生成  |
|  検査陽性者の状況  |  main_summary  |　https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv を集計 |  covid19_data.pyで生成  |
|  陽性患者数（日別）  |  patients_summary  | https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv を集計 |  covid19_data.pyで生成  |
|  日別患者増減数  |  current_patients  | https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv を集計 |  covid19_data.pyで生成  |
|  治療修了者数  |  discharges_summary  | https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv を集計 |  covid19_data.pyで生成  |
|  日別検査数  |  inspections  | https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv を集計 |  covid19_data.pyで生成  |
|  陽性患者の属性  |  patients  | https://www.harp.lg.jp/opendata/dataset/1369/resource/2828/patients.csv |  main.pyで生成  |
|  日別窓口相談件数（札幌市保健所）  |  contacts  | https://ckan.pf-sapporo.jp/dataset/f6338cc2-dd6b-43b6-98a3-cd80b05b6a36/resource/e9e6f062-cafd-4aea-992f-039e2e26f4ac/download/contacts.csv |  main.pyで生成  |
|  日別電話相談件数 （札幌市保健所） |  querents  | https://ckan.pf-sapporo.jp/dataset/f6338cc2-dd6b-43b6-98a3-cd80b05b6a36/resource/a89ba566-93d1-416a-a269-e0ba48a06636/download/querents.csv |  main.pyで生成  |

## Scheduling
GitHub Actionsにより1時間に一度、すべてjson類をgh-pagesブランチに書き出します

## 外部からのアクセス
gh-pagesブランチにあるjsonデータに直接アクセスしてデータを読み出す事が出来ます。
sample1: https://codeforsapporo.github.io/covid19hokkaido_scraping/patients.json
sample2: https://raw.githubusercontent.com/codeforsapporo/covid19hokkaido_scraping/gh-pages/patients.json