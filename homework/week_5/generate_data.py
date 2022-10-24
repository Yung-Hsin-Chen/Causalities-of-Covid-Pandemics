import pandas as pd
from datetime import datetime

shape = 1000000
time_lst = []

col_1_and_2 = [i for i in range(shape)]
col_3 = ["a" for i in range(shape)]
col_4 = ["b" for i in range(shape)]
col_5 = ["c" for i in range(shape)]

df_dict = {
    "col_1": col_1_and_2,
    "col_2": col_1_and_2,
    "col_3": col_3,
    "col_4": col_4,
    "col_5": col_5
}

df = pd.DataFrame(df_dict)

## WRITE TO FILES
# HDF
start_time = datetime.now()
df.to_hdf("homework/week_5/data.h5", key="df")  
end_time = datetime.now()
time_lst.append(end_time - start_time)

# FEATHER
start_time = datetime.now()
df.to_feather("homework/week_5/data.feather") 
end_time = datetime.now()
time_lst.append(end_time - start_time)

# PARQUET
start_time = datetime.now()
df.to_parquet("homework/week_5/data.gzip") 
end_time = datetime.now()
time_lst.append(end_time - start_time)

## WRITE TIME TO TXT
with open("homework/week_5/time_used.txt", "w") as f:
    f.write("HDF: " + str(time_lst[0]) + "\n")
    f.write("Feather: " + str(time_lst[1]) + "\n")
    f.write("Parquet: " + str(time_lst[2]) + "\n")
