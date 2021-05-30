import pandas as pd

csv_df = pd.read_csv("../csv/Ratings_Warriner_et_al.csv")

for i in range (1,15):
    max_n = i * 1000
    min_n = (i-1) * 1000
    split_csv_df = csv_df.iloc[min_n:max_n,:]
    split_csv_df.to_csv("../csv/split/{}.csv".format(i), index=False)
