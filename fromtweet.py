from requests_oauthlib import OAuth1Session
import json
import re
import datetime
CK = '8zmtH9NW3RMordGP2N3aGN8aJ'
CS = 'xeGGLyTl2a4WLUPFMApmJ7SJMXup6QycRURKs31CHSLR665qQn'
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
twitter = OAuth1Session(CK, CS)
params = {'screen_name' : '@suzukinaomichi', 'count' : 5, 'tweet_mode': 'extended'}

req = twitter.get(url, params = params)

search_timeline = json.loads(req.text)
for tweet in search_timeline:
    created_at = tweet['created_at']
    text = tweet['full_text']


    if re.search("検査人数",text):
        print(created_at)
        print(text)
        date = re.search("(\d+)月(\d+)日",text)
        date_time = datetime.datetime(2020, int(date.group(1),10), int(date.group(2),10))
        date_str = date_time.isoformat()
        print('Date: ', date_str)
        inspections = re.search("検査人数 (\d+)（\+(\d+)）",text)
        print(inspections.group(1))
        print(inspections.group(2))
        inspections_summary = re.search("陽性累計 (\d+)（\+(\d+)）",text)
        print(inspections_summary.group(1))
        print(inspections_summary.group(2))
        better_patients_summary = re.search("陰性確認済累計 (\d+)（\+(\d+)）",text)
        print(better_patients_summary.group(1))
        print(better_patients_summary.group(2))
        better_patients_summary_1 = re.search("死亡累計 (\d+)",text)
        print(better_patients_summary_1.group(1))
        better_patients_summary_2 = re.search("現在患者数 (\d+)（\+(\d+)）",text)
        print(better_patients_summary_2.group(1))
        print(better_patients_summary_2.group(2))
        better_patients_summary_3 = re.search("軽症・中等症 (\d+)",text)
        print(better_patients_summary_3.group(1))
        better_patients_summary_4 = re.search("重症 (\d+)",text)
        print(better_patients_summary_4.group(1))
        break

