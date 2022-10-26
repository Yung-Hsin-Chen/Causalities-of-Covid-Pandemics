import requests
import datetime
import pandas as pd
import time
import datetime

def get_kline(currency_pair="BTCUSDT", date="01/09/22"):
    """
    This function retrieves 75 observations of klines data for a generic currency pair since a generic date.
    Arguments:
        currency_pair: a string. a generic currency pair.
        date: a string. a date (dd/mm/yyyy) separated by "/".
    Return:
        if succeeded:
            df: a dataframe. df is also saved in ./data_retrieved.
        else:
            None
    """
    # GET TIMESTAMP
    startTime_str = str(int(time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())))

    # GET OTHER PARAMETERS
    ROOT_URL_str = "https://api.binance.com"
    endpoint_str = "api/v3/klines"
    symbol_str = currency_pair
    interval_str = "1d"

    # CONSTRUCT REQUEST URL
    req = "{root_url}/{endpoint}?symbol={symbol}&interval={interval}&startTime={startTime}" \
        .format(root_url=ROOT_URL_str, \
                endpoint=endpoint_str, \
                symbol=symbol_str, \
                interval=interval_str, \
                startTime=startTime_str)
    # https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&startTime=1661983200

    resp = requests.get(req)
    # SHOULD BE <Response [200]> IF SUCCEEDED

    # CONVERT TO DF
    if str(resp) == "<Response [200]>":
        data = resp.json()[:75]
        column_lst = ["Kline open time", "Open price", "High price", "Low price", "Close price", \
                    "Volume", "Kline Close time", "Quote asset volume", "Number of trades", \
                    "Taker buy base asset volume", "Taker buy quote asset volume", "Unused field, ignore"]
        df = pd.DataFrame(data, columns=column_lst)
        ## RUN THIS LINE IF YOU WISH TO WRITE THE DF TO CSV IN ./DATA_RETRIEVED
        # df.to_csv("homework/week_6/data_retrieved/kline.csv", index=False)
        print("Data retrieve successfully and saved!")
        return df
    else:
        return None


get_kline("BTCUSDT", "01/09/2022")