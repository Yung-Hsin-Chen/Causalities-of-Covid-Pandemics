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
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

class ModelTraining:

    def __init__(self, X_train, y_train):
        self._X_train = X_train
        self._y_train = y_train

    def train_model_lr(self):
        model = LogisticRegression(penalty="l2", solver="newton-cg")
        model.fit(self._X_train, self._y_train)
        with open(os.path.join(os.path.abspath(""), "models", "model_logi.sav"), "wb") as f:
            pickle.dump(model, f)
        return

    def train_model_perc(self):
        model = Perceptron(tol=1e-3, random_state=0)
        model.fit(X_train, y_train)
        with open(os.path.join(os.path.abspath(""), "models", "model_perc.sav"), "wb") as f:
            pickle.dump(model, f)
        return 

    def train_model_xgb(self):
        clf = GradientBoostingClassifier()
        param_grid = {"loss": ["log_loss", "deviance", "exponential"], \
                      "learning_rate": [0.1, 0.01, 0.001, 0.0001], \
                      "n_estimators": [50, 100, 200, 300], \
                      "max_depth": [1, 2, 3, 4], \
                      "random_state": [21, 42]}
        model = GridSearchCV(clf, param_grid, cv=5, n_jobs=1, verbose=1)
        model.fit(self._X_train, self._y_train)
        with open(os.path.join(os.path.abspath(""), "models", "model_xgbo.sav"), "wb") as f:
            pickle.dump(model, f)



if __name__ == "__main__":
    df = pd.read_hdf(os.path.join(os.path.abspath(""), "data", "processed", "covid_data.h5"))
    pickle.dump(df.columns[:-1], open(os.path.join(os.path.abspath(""), "models", "feature_list.pkl"), "wb"))
    X_train, X_test, y_train, y_test = data_splitting(df)
    model_training = ModelTraining(X_train, y_train)
    model_training.train_model_lr()
    model_training.train_model_perc()
    model_training.train_model_xgb()
    