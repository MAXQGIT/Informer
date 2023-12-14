from utils.timefeatures import time_features
import pandas as pd

df = pd.read_csv("datasets/Weather_all_202311.csv")
df["date"] = df["timeid"]
df_time = df["date"]
df_time = pd.DataFrame(df_time)
df_timestampe  = time_features(df_time, timeenc=1, freq="s")