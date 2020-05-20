import mat4py
import pandas as pd
from scipy import signal

data = mat4py.loadmat('666200402020631.mat')

data_keys = data.keys()

master_df = pd.DataFrame(data=None)
for key in data_keys:
    print(key)
    print(data[key]["Description"])
    df = pd.DataFrame([data[key]["data"]], columns=[key])
    master_df = master_df.merge(df, how="outer", left_index=True, right_index=True)


master_df.to_csv("Var_Keywwords.csv", index=False)
