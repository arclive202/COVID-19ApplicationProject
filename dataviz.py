import pandas as pd

india_data_url = "https://www.mohfw.gov.in/data/datanew.json"
df = pd.read_json(india_data_url)
df.set_index('state_name', inplace=True)
df.drop(columns='sno', axis=1, inplace=True)
print(df.index)

#df.reset_index(inplace=True)




