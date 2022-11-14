import pandas as pd
import requests
import io

def request_external_data():
    # LIST OF URLS WITH DATA TO BE RETIEVED
    url_lst = ["https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_deaths_per_million.csv",
               "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/hospitalizations/covid-hospitalizations.csv",
               "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-age-group.csv",
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
