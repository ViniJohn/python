import pandas as pd
import numpy as np

df_wk14 = pd.read_csv(r'\\pl-filesrv\Data\Public\Freeze Plan\TXT\Software\IMPORT_INCREMENTAL\Archive\INC_JITUPLOAD_20210413110200_1.txt',sep=';')
df_wk15 = pd.read_csv(r'\\pl-filesrv\Data\Public\Freeze Plan\TXT\Software\IMPORT_INCREMENTAL\Archive\INC_JITUPLOAD_20210407110200_1.txt',sep=';')

frames = [df_wk14,df_wk15]

df_data = pd.concat(frames,axis=1, keys=["wk14","wk15"])

print(df_data)