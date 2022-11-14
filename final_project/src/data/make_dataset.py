# -*- coding: utf-8 -*-
import os
from data_transform import request_external_data

def main():
    """ 
    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    # CHECK IF ./data/ DIRECTORY EXISTS
    if os.path.isdir("./data/") == False:
        os.mkdir("./data")
        os.mkdir("./data/external")
        os.mkdir("./data/processed")

    request_external_data()

    return


if __name__ == '__main__':

    main()
