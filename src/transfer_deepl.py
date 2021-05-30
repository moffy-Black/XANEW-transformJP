import urllib.request
import urllib.parse
import os
import sys
import json
import pandas as pd

with open("../config/config.json") as j:
    config = json.load(j)

api_key = config['deepl_key']
base_url = "https://api-free.deepl.com/v2/translate"

def trans_ja(text, s_lang='EN', t_lang='JA'):
    headers = {
        'Context-Type': 'application/x-www-form-urlencoded; utf-8'
    }

    params = {
        'auth_key': api_key,
        'text': text,
        'target_lang': t_lang
    }

    req = urllib.request.Request(
        base_url,
        method = 'POST',
        data = urllib.parse.urlencode(params).encode('utf-8'),
        headers=headers
    )

    try:
        with urllib.request.urlopen(req) as res:
            res_json = json.loads(res.read().decode('utf-8'))
            translated_text = res_json['translations'][0]['text']
            return translated_text
    except urllib.error.HTTPError as e:
        print(e)

if __name__ == '__main__':
    df = pd.read_csv("../csv/split/11.csv")
    array = []
    [array.append(trans_ja(df['Word'][i])) for i in range(1000)]
    s = pd.Series(data = array, name="deepltrans_ja")
    concat_df = pd.concat([df, s],axis=1)
    concat_df.to_csv("../csv/translated_csv/11.csv",index=False)

    df = pd.read_csv("../csv/split/12.csv")
    array = []
    [array.append(trans_ja(df['Word'][i])) for i in range(1000)]
    s = pd.Series(data = array, name="deepltrans_ja")
    concat_df = pd.concat([df, s],axis=1)
    concat_df.to_csv("../csv/translated_csv/12.csv",index=False)

    df = pd.read_csv("../csv/split/13.csv")
    array = []
    [array.append(trans_ja(df['Word'][i])) for i in range(1000)]
    s = pd.Series(data = array, name="deepltrans_ja")
    concat_df = pd.concat([df, s],axis=1)
    concat_df.to_csv("../csv/translated_csv/13.csv",index=False)

    df = pd.read_csv("../csv/split/14.csv")
    array = []
    [array.append(trans_ja(df['Word'][i])) for i in range(915)]
    s = pd.Series(data = array, name="deepltrans_ja")
    concat_df = pd.concat([df, s],axis=1)
    concat_df.to_csv("../csv/translated_csv/14.csv",index=False)