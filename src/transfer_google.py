import numpy as np
import pandas as pd
from googletrans import Translator

def trans_ja(text):
    translator = Translator(service_urls=[
        'translate.google.com'
    ])
    translated = translator.translate(text,src='en',dest="ja")
    return translated.text

if __name__ == '__main__':
    df = pd.read_csv("../csv/Ratings_Warriner_et_al.csv")
    x = 0
    array = []
    for i in range(0, 1000):
        x += 1
        array.append(trans_ja(df["Word"][i]))
    s = pd.Series(data = array)
    s.to_csv("../csv/JA_Ratings_Warriner_et_al.csv")
    print(x)