import os
import pandas as pd

filename = "C:\\Users\\aditya.roychoudhary\\Desktop\\Country\\Countries.csv"
    


for root, dirs, files in os.walk("C:\\Users\\aditya.roychoudhary\\Desktop\\Country\\"):
    for file in files:
        if file.endswith(".csv"):
            tempdf = pd.read_csv(os.path.join(root, file))
            if not os.path.isfile(filename):
                tempdf.to_csv(filename, header='column_names')
            else:
                tempdf.to_csv(filename, mode='a', header=False)
            del tempdf
            