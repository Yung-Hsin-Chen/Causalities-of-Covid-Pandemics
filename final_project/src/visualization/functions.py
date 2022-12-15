import pandas as pd
import os
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from mpl_toolkits.axes_grid1 import make_axes_locatable

def pickle_load(file_name: str):
    with open(os.path.join("..", "models", file_name), "rb") as f:
        data = pickle.load(f)
    return data

def data_splitting(df):
    label = "total_cases_per_million_level"
    y = df[label]
    X = df[df.columns.drop(label)]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21)
    return X_train, X_test, y_train, y_test

def loading_data():
    df_raw = pd.read_hdf(os.path.join("..", "data", "external", "owid-covid-data.h5"))
    df = pd.read_hdf(os.path.join("..", "data", "processed", "covid_data.h5"))
    feature_importance = pd.read_hdf(os.path.join("..", "models", "feature_importance.h5"))
    model_acc_summary = pd.read_hdf(os.path.join("..", "models", "model_acc_summary.h5"))
    feature_list = pickle_load("feature_list.pkl")
    lr_y_test_pred = np.load(os.path.join("..", "models", "lr_y_test_pred.npy"))
    perc_y_test_pred = np.load(os.path.join("..", "models", "perc_y_test_pred.npy"))
    xgbo_y_test_pred = np.load(os.path.join("..", "models", "xgbo_y_test_pred.npy"))
    model_logi = pickle_load("model_logi.sav")
    model_perc = pickle_load("model_perc.sav")
    model_xgbo = pickle_load("model_xgbo.sav")
    X_train, X_test, y_train, y_test = data_splitting(df)
    return df_raw, df, feature_importance, model_acc_summary, feature_list, \
           lr_y_test_pred, perc_y_test_pred, xgbo_y_test_pred, model_logi, \
           model_perc, model_xgbo

def plot_label_bar(df: pd.DataFrame) -> None:
    y_lst = df["total_cases_per_million_level"].value_counts().tolist()
    x = np.arange(len(y_lst))
    plt.bar(x, y_lst)
    plt.title("Labels")
    plt.xlabel("labels")
    plt.ylabel("data size")
    plt.xticks(x, ["level 1", "level 2", "level 3", "level 4"])
    plt.show()
    return

def plot_box_quantile(df: pd.DataFrame, col_name: str) -> None:
    df = df.loc[df[col_name] > 0]
    df.boxplot(col_name, vert=False)
    plt.show()
    print("quantile: \n")
    print(df[col_name].quantile([0.25, 0.5, 0.75]))
    return

def plot_scatter(df: pd.DataFrame, col_1: str, col_2: str, x_min=None, x_max=None, y_min=None, y_max=None) -> None:
    lim = [x_min, x_max, y_min, y_max]
    ax = df.plot.scatter(x=col_1, y=col_2)
    if any(lim):
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
    plt.show()
    return

def plot_data_cnt_of_countries(df: pd.DataFrame, boundary: int):
    df = df.groupby(["location"])[["date"]].count().rename(columns={"date": "count"}).reset_index()
    country_less = df[df["count"] < boundary]["location"].tolist()
    print("Countries with less than "+str(boundary)+" data entries will not be used: ", 
          " ".join(country_less), "\n")
    print("Data Counts of Countries:")
    display(df)
    return

def plot_corr(df: pd.DataFrame, feature_list):
    plt.matshow(df.corr(), cmap="bone")
    plt.xticks(range(11), feature_list.tolist(), rotation=90)
    plt.yticks(range(11), feature_list.tolist(), rotation=0)
    cb = plt.colorbar(fraction=0.046, pad=0.04)
    cb.ax.tick_params(labelsize=10)
    plt.show()
    return
