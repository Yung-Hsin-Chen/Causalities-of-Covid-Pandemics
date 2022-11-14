import pandas as pd
from connect import DATAPATH
import os

def get_covid_data():
    hospital_df = pd.read_hdf(DATAPATH+"/external/covid-hospitalizations.h5")
    death_df = pd.read_hdf(DATAPATH+"/external/new_deaths_per_million.h5")
    vacc_age_df = pd.read_hdf(DATAPATH+"/external/vaccinations-by-age-group.h5")
    vacc_manu_df = pd.read_hdf(DATAPATH+"/external/vaccinations-by-manufacturer.h5")
    covid_df = pd.read_hdf(DATAPATH+"/external/owid-covid-data.h5")
    return hospital_df, death_df, vacc_age_df, vacc_manu_df, covid_df

if __name__ == "__main__":

    get_covid_data()