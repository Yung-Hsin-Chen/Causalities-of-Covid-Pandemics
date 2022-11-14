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

country_data_count()


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()