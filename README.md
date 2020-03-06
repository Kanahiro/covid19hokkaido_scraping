## What is this
http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm
上記サイトをBeautifulSoupによりスクレイピングし、得たtableのデータを変換してjsonやcsvとして出力するPythonスクリプトです

## Scheduling
GitHub Actionsにより15分に一度、main.pyを実行してjsonやcsv類をgh-pagesブランチに書き出します