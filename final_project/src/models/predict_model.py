import os
import sys
parentdir = os.path.dirname("final_project")
sys.path.insert(0, parentdir)
from src.models.data_splitting import data_splitting
import pickle
import pandas as pd
import numpy as np


class Prediction:

    def __init__(self, X_test, y_test):
        self._X_test = X_test
        self._y_test = y_test
        self._model_lr_acc = 0
        self._model_perc_acc = 0
        self._model_tree_acc = 0

    def get_accuracy(self, y_test_pred):
        correct = 0

        for i, v in enumerate(list(self._y_test)):
            if v == y_test_pred[i]:
                correct += 1
        return correct/len(self._y_test)

    def predict_model_lr(self):
        model = pickle.load(open(os.path.join(os.path.abspath(""), "models", "model_logi.sav"), "rb"))
        y_test_pred = model.predict(self._X_test)
        self._model_lr_acc = self.get_accuracy(y_test_pred)
        np.save(os.path.join(os.path.abspath(""), "models", "lr_y_test_pred.npy"), y_test_pred)
        return

    def predict_model_perc(self):
        model = pickle.load(open(os.path.join(os.path.abspath(""), "models", "model_perc.sav"), "rb"))
        y_test_pred = model.predict(self._X_test)
        self._model_perc_acc = self.get_accuracy(y_test_pred)
        np.save(os.path.join(os.path.abspath(""), "models", "perc_y_test_pred.npy"), y_test_pred)
        return

    def predict_model_tree(self):
        model = pickle.load(open(os.path.join(os.path.abspath(""), "models", "model_xgbo.sav"), "rb"))
        y_test_pred = model.predict(self._X_test)
        self._model_tree_acc = self.get_accuracy(y_test_pred)
        np.save(os.path.join(os.path.abspath(""), "models", "xgbo_y_test_pred.npy"), y_test_pred)
        return

    def get_model_accuracy(self):
        self.predict_model_lr()
        self.predict_model_perc()
        self.predict_model_tree()
        model_acc = pd.DataFrame.from_dict({"logistic regression":[self._model_lr_acc],
                                            "perceptron":[self._model_perc_acc],
                                            "xgboost":[self._model_tree_acc]})
        model_acc.to_hdf(os.path.join(os.path.abspath(""), "models", "model_acc_summary.h5"), key="df", mode="w", format="t")
        return model_acc

if __name__ == "__main__":
    df = pd.read_hdf(os.path.join(os.path.abspath(""), "data", "processed", "covid_data.h5"))
    X_train, X_test, y_train, y_test = data_splitting(df)
    prediction = Prediction(X_test, y_test)
    model_acc = prediction.get_model_accuracy()
    print(model_acc)
