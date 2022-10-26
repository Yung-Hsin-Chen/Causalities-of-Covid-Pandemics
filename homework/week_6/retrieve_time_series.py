import requests
import datetime
import pandas as pd
import time
import datetime


def generate_unemployment_rate_query_string(api_key):
    """
    This function construct a query string to retrieve the series of the monthly 
    unemployment rate (seasonally adjusted) since 2020-01 with API key provided.
    Arguments:
        api_key: a string. API key from FRED.
    return:
        req: a string. the target query string.
    """
    ROOT_URL_str = "https://api.stlouisfed.org/"
    endpoint_str = "fred/series/observations"
    series_id_str = "UNRATE"
    api_key_str = api_key
    observation_start_str = "2020-01-01"
    file_type_str = "json"

    req = "{root_url}/{endpoint}?series_id={series_id}&api_key={api_key}&\
        observation_start={observation_start}&file_type={file_type}" \
        .format(root_url=ROOT_URL_str, \
                endpoint=endpoint_str, \
                series_id=series_id_str, \
                api_key=api_key_str, \
                observation_start=observation_start_str, \
                file_type=file_type_str)

    return req
    # https://api.stlouisfed.org//fred/series/observations?series_id=UNRATE&api_key=abc123&observation_start=2020-01-01&file_type=json

req = generate_unemployment_rate_query_string("abc123")


################################### SAVE DATA AS DF HERE ####################################

resp = requests.get(req)
# SHOULD BE <Response [200]> IF SUCCEEDED

data = resp.json()["observations"]
column_lst = ["realtime_start", "realtime_end", "date", "value"]
df = pd.DataFrame(data, columns=column_lst)[["date", "value"]].rename(columns={"value": "unemployment rate"})

