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
|  検査陽性者の状況  |  main_summary  | 北海道オープンデータポータル |  inspections, patients_summary, current_patientsを集計  |
|  陽性患者の属性  |  patients  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2828/patients.csv  |
|  陽性患者数（日別）  |  patients_summary  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2828/patients_summary.csv  |
|  日別患者増減数  |  current_patients  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2828/current_patients.csv  |
|  治療修了者数  |  discharges_summary  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2828/discharges_summary.csv  |
|  日別検査数  |  inspections  | 北海道オープンデータポータル |  https://www.harp.lg.jp/opendata/dataset/1369/resource/2828/inspections.csv  |
|  日別窓口相談件数（札幌市保健所）  |  contacts  | DATA SMART CITY SAPPORO |  https://ckan.pf-sapporo.jp/dataset/covid_19_soudan  |
|  日別電話相談件数 （札幌市保健所） |  querents  | DATA SMART CITY SAPPORO |  https://ckan.pf-sapporo.jp/dataset/covid_19_soudan  |

## Scheduling
GitHub Actionsにより1時間に一度、main.pyを実行してjson類をgh-pagesブランチに書き出します

## 外部からのアクセス
gh-pagesブランチにあるjsonデータに直接アクセスしてデータを読み出す事が出来ます。
sample: https://raw.githubusercontent.com/codeforsapporo/covid19hokkaido_scraping/gh-pages/patients.json

## webへのデータ更新方法
初回のみ
1. 自分のgithubのアカウントにcovid19のほうのリポジトリをfork
2. git をインストール
3. git clone -b gh-pages https://github.com/codeforsapporo/covid19hokkaido_scraping.git
4. git clone https://github.com/codeforsapporo/covid19.git
5. cd covid19
6. git remote add fork https://<username>:<password>@github.com/<username>/covid19.git
7. cd ../

その後は2回目以降と同様
2回目以降

1. cd covid19
2. git pull
3. cd ../
4. cd covid19hokkaido_scraping
5. git pull
6. cd ../
7. covid19hokkaido_scraping内のjsonファイルをすべてcovid19/dataのjsonファイルに上書き
8. cd covid19
9. git add .
10. git commit -m 'UpdateData'
11. git push fork development
12. githubからbase repositoryをcodeforsapporo/covid19 development 、　head repositoryを :<username>/covid19 developmetに設定
13. create pull request
14. わかりやすいpullrequest名を入れcreate pull request