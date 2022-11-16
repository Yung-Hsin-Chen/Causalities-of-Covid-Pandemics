# -*- coding: utf-8 -*-
import os
import sys
parentdir = os.path.dirname("final_project")
sys.path.insert(0, parentdir)
from datafeed.downstream import get_covid_data
from src.data.data_transform import CleanData

def main():
    """ 
    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """

    df_lst = get_covid_data()

    clean_data = CleanData(df_lst)
    df_lst = clean_data.clean_data()
    # vacc_age_df, vacc_manu_df, covid_df = get_covid_data



    return df_lst


if __name__ == '__main__':

    main()