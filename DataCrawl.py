import pandas as pd
import requests
from datetime import datetime
import os

url = "https://www.worldometers.info/coronavirus/"
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
df.fillna(0,inplace=True)
now = datetime.now()
current_time = now.strftime("%d-%m-%y %H:%M")
df["TimeOfReport"] = current_time
df.head()



for i in range(len(df)):
    print("The row number ",i,"  \n",df.iloc[i,0], "\n\n\n\n")
    filename = "C:\\Users\\aditya.roychoudhary\\Desktop\\Country\\" + df.iloc[i,0] + ".csv"
    if not os.path.isfile(filename):
        df.iloc[i:i+1].to_csv(filename, header='column_names')
    else:
        df.iloc[i:i+1].to_csv(filename, mode='a', header=False)