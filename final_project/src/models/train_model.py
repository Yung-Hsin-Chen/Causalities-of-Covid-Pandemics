import os
import sys
parentdir = os.path.dirname("final_project")
sys.path.insert(0, parentdir)
from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd
from src.models.data_splitting import data_splitting
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeRegressor

class ModelTraining:

    def __init__(self, X_train, y_train):
        self._X_train = X_train
        self._y_train = y_train

    def train_model_lr(self):
        model = LogisticRegression(penalty="l2", solver="newton-cg")
        model.fit(self._X_train, self._y_train)
        pickle.dump(model, open(os.path.join(os.path.abspath(""), "models", "model_logi.sav"), "wb"))
        return

    def train_model_perc(self):
        model = Perceptron(tol=1e-3, random_state=0)
        model.fit(X_train, y_train)
        pickle.dump(model, open(os.path.join(os.path.abspath(""), "models", "model_perc.sav"), "wb"))
        return 

    def train_model_tree(self):
        model = DecisionTreeRegressor()
        model.fit(X_train, y_train)
        pickle.dump(model, open(os.path.join(os.path.abspath(""), "models", "model_deci.sav"), "wb"))
        return



if __name__ == "__main__":
    df = pd.read_hdf(os.path.join(os.path.abspath(""), "data", "processed", "covid_data.h5"))
    pickle.dump(df.columns[:-1], open(os.path.join(os.path.abspath(""), "models", "feature_list.pkl"), "wb"))
    X_train, X_test, y_train, y_test = data_splitting(df)
    model_training = ModelTraining(X_train, y_train)
    model_training.train_model_lr()
    model_training.train_model_perc()
    model_training.train_model_tree()
    