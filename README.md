## What is this
インターネット上の北海道のコロナウィルス情報をBeautifulSoupによりスクレイピングし、得たtableのデータを変換してjsonやcsvとして出力するPythonスクリプトです

## Specification
- main.pyを実行すると、csvとjsonを出力します
- 実装済データのみ、csvファイルが出力されます
- jsonファイルの構造は、都公式リポジトリのdata.jsonに準拠しています
- 実装済データのみ、jsonファイルにデータが追記されます

#### 実装済データとソースは以下のとおりです
- patients
- patients_summary
http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm

- last_update
main.py実行時点の日時

## Scheduling
GitHub Actionsにより15分に一度、main.pyを実行してjsonやcsv類をgh-pagesブランチに書き出します