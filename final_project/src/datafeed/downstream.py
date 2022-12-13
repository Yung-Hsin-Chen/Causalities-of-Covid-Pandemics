import pandas as pd
from datafeed.connect import DATAPATH
import os

def get_covid_data():

    covid_df = pd.read_hdf(os.path.join(DATAPATH, "external", "owid-covid-data.h5"))

    return covid_df

if __name__ == "__main__":

    get_covid_data()