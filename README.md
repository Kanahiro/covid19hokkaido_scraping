## What is this
インターネット上の北海道のコロナウィルス情報をスクレイピングし、得たデータを変換してjsonやcsvとして出力するPythonスクリプトです

## Specification
- main.pyを実行すると、①スクレイピング実装済データのソースにアクセスし、②importフォルダ内のcsvを読み込んで、jsonファイルとcsvファイルを出力します
- 出力されるファイルの構造は、[都公式リポジトリ](https://github.com/tokyo-metropolitan-gov/covid19)に準拠しています
- importフォルダ内のcsvファイル名は、都公式リポジトリに準拠している必要があります
- スクレイピング実装済データとcsvファイルの分だけ、jsonファイルとcsvファイルが出力されます
- スクレイピング実装済で、csvファイルもある場合、csvファイルのデータが優先されます

#### スクレイピング実装済データとソースは以下のとおりです
- patients:http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm
- patients_summary:http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm

## Scheduling
GitHub Actionsにより15分に一度、main.pyを実行してjsonやcsv類をgh-pagesブランチに書き出します