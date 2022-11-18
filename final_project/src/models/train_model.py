import os
import sys
parentdir = os.path.dirname("final_project")
sys.path.insert(0, parentdir)
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd
from src.models.data_splitting import data_splitting
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeRegressor

class ModelTraining:

    def __init__(self, X_train, X_test, y_train, y_test):
        self._X_train = X_train
        self._X_test = X_test
        self._y_train = y_train
        self._y_test = y_test

    def train_model_lr(self):
        clf = Pipeline([("standardise", StandardScaler()), ("clf", LogisticRegression())])
        param_grid = {"clf__penalty": ["l2"], \
              "clf__solver": ["newton-cg", "lbfgs", "liblinear"]}

        model = GridSearchCV(clf, param_grid, cv=5, n_jobs=None, verbose=1)
        model.fit(self._X_train, self._y_train)
        best_para = model.best_params_
        model_importance = LogisticRegression(penalty=best_para["clf__penalty"], \
                                   solver=best_para["clf__solver"])
        pickle.dump(model_importance, open(os.path.abspath("")+"/models/model_lr.sav", "wb"))
        return

    def train_model_mlp(self):
        model = Perceptron(tol=1e-3, random_state=0)
        model.fit(X_train, y_train)
        pickle.dump(model, open(os.path.abspath("")+"/models/model_perc.sav", "wb"))
        return 

    def train_model_tree(self):
        model = DecisionTreeRegressor()
        model.fit(X_train, y_train)
        pickle.dump(model, open(os.path.abspath("")+"/models/model_tree.sav", "wb"))
        return



if __name__ == "__main__":
    df = pd.read_hdf(os.path.abspath("")+"/data/processed/covid_data.h5")
    X_train, X_test, y_train, y_test = data_splitting(df)
    model_training = ModelTraining(X_train, X_test, y_train, y_test)
    model_training.train_model_lr()
    model_training.train_model_mlp()
    