import csv
import pandas as pd

path = r'C:\Users\adamv\Desktop\adjust.csv'

df = pd.read_csv(path)

df["Position"] = df["Position"] * 3

df.to_csv(path,index=False)