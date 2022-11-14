import matplotlib.pyplot as plt
import pandas as pd

def country_data_count():
    df = pd.read_hdf("./data/external/owid-covid-data.h5")
    df_count = df.groupby(["location"])[["iso_code"]].count().rename(columns={"iso_code": "count"}).reset_index()
    df_count = df_count.sort_values("count")

    plt.figure(figsize=(4,45))
    plt.style.use('ggplot')

    plt.barh(df_count["location"].tolist(), df_count["count"].tolist())
    plt.title("Data Counts for Each Country")
    plt.ylabel("country")
    plt.xlabel("count")
    plt.savefig("src/visualization/visualize_figures/data_count.png", format="png")
    plt.show()

    return



if __name__ == '__main__':

    country_data_count()