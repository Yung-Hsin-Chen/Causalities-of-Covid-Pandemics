# -*- coding: utf-8 -*-
import os
import sys
parentdir = os.path.dirname("final_project")
sys.path.insert(0, parentdir)
from datafeed.downstream import get_covid_data
from src.features.data_cleaning import CleanData
from src.features.prepare_label import PrepareLabel

covid_df = get_covid_data()
clean_data = CleanData(covid_df)

def build_feature(clean_data:CleanData):
    """ 
    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    covid_df = clean_data.apply_clean_data()
    prepare_label = PrepareLabel(covid_df)
    df_output = prepare_label.apply_prepare_label()
    del df_output["location"]
    df_output = df_output.fillna(0)
    df_output.to_hdf(os.path.join(os.path.abspath(""), "data", "processed", "covid_data.h5"), key="df", mode="w", format="t")

    return


if __name__ == '__main__':

    build_feature(clean_data)
