import pandas as pd
import requests
import io
import os
from connect import DATAPATH

def put_covid_data():

    # CHECK IF ./data/ DIRECTORY EXISTS
    if os.path.isdir(DATAPATH) == False:
        os.mkdir(DATAPATH)
        os.mkdir(DATAPATH+"/external")
        os.mkdir(DATAPATH+"/processed")

    url_lst = ["https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-age-group.csv",
                "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-manufacturer.csv",
                "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"]

    for url in url_lst:

        data = requests.get(url).content

        # TURN REQUESTED DATA TO DATAFRAME
        df_name = url[url.rfind("/")+1:url.rfind(".")]
        df = pd.read_csv(io.StringIO(data.decode("utf-8")))

        # CONVERT MIXTYPE COLUMNS TO STR
        if df_name == "owid-covid-data":
            col_lst = ['iso_code', 'continent', 'location', 'date', 'tests_units']
            df.loc[:,col_lst] = df[col_lst].applymap(str)
            
        df.to_hdf("./data/external/"+df_name+".h5", key='df', mode='w') 
    
    return

if __name__ == "__main__":

    put_covid_data()
