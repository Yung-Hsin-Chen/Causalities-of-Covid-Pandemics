import pandas as pd
from datafeed.connect import DATAPATH

def get_covid_data():

    vacc_age_df = pd.read_hdf(DATAPATH+"/external/vaccinations-by-age-group.h5")
    vacc_manu_df = pd.read_hdf(DATAPATH+"/external/vaccinations-by-manufacturer.h5")
    covid_df = pd.read_hdf(DATAPATH+"/external/owid-covid-data.h5")

    return [vacc_age_df, vacc_manu_df, covid_df]

if __name__ == "__main__":

    get_covid_data()