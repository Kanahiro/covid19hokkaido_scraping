## What is this
インターネット上の北海道のコロナウィルス情報をスクレイピングし、得たデータを変換してjsonやcsvとして出力するPythonスクリプトです

## Specification
- main.pyを実行すると、①settings.pyのREMOTE_SOURCESに基づき外部データを取得し、②importフォルダ内のcsvを読み込んで、データの数だけjsonファイルを出力します
- jsonの出力前に、データのカラム名は[北海道 新型コロナウイルスまとめサイト](https://github.com/codeforsapporo/covid19)に準拠するよう変換されます(settings.pyのHEADER_TRANSLATIONSに基づきます)
- settings.pyとimportフォルダ内に、同じkeyがある場合、importフォルダが優先されます

## 現在実装されているデータ
|  data  |  source  | url  |
| ---- | ---- | ---- |
|  patients  | ODP |  https://www.harp.lg.jp/opendata/api/package_show?id=752c577e-0cbe-46e0-bebd-eb47b71b38bf  |
|  patients_summary  | ODP |  https://www.harp.lg.jp/opendata/api/package_show?id=752c577e-0cbe-46e0-bebd-eb47b71b38bf  |
|  contacts  | CKAN(CSV) |  https://ckan.pf-sapporo.jp/dataset/f6338cc2-dd6b-43b6-98a3-cd80b05b6a36/resource/e9e6f062-cafd-4aea-992f-039e2e26f4ac/download/contacts.csv  |
|  querents  | CKAN(CSV) |  https://ckan.pf-sapporo.jp/dataset/f6338cc2-dd6b-43b6-98a3-cd80b05b6a36/resource/a89ba566-93d1-416a-a269-e0ba48a06636/download/querents.csv  |
|  current_patients  | ODP |  https://www.harp.lg.jp/opendata/api/package_show?id=752c577e-0cbe-46e0-bebd-eb47b71b38bf  |
|  discharges_summary  | ODP |  https://www.harp.lg.jp/opendata/api/package_show?id=752c577e-0cbe-46e0-bebd-eb47b71b38bf  |

## Scheduling
GitHub Actionsにより15分に一度、main.pyを実行してjson類をgh-pagesブランチに書き出します