import os
import sys
parentdir = os.path.dirname("final_project")
sys.path.insert(0, parentdir)
from src.models.data_splitting import data_splitting
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score


class Prediction:

    def __init__(self, X_test, y_test):
        self._X_test = X_test
        self._y_test = y_test
        self._model_lr_acc = 0
        self._model_perc_acc = 0
        self._model_tree_acc = 0
        self._model_lr_f1 = 0
        self._model_perc_f1 = 0
        self._model_tree_f1 = 0

    def get_accuracy(self, y_test_pred):
        correct = 0

        for i, v in enumerate(list(self._y_test)):
            if v == y_test_pred[i]:
                correct += 1
        return correct/len(self._y_test)
    
    def get_f1_score(self, y_test_pred):
        macro_f1 = f1_score(list(self._y_test), y_test_pred, average="macro")
        micro_f1 = f1_score(list(self._y_test), y_test_pred, average="micro")
        return (macro_f1, micro_f1)

    def predict_model_lr(self):
        model = pickle.load(open(os.path.join(os.path.abspath(""), "models", "model_logi.sav"), "rb"))
        y_test_pred = model.predict(self._X_test)
        self._model_lr_acc = self.get_accuracy(y_test_pred)
        self._model_lr_f1 = self.get_f1_score(y_test_pred)
        np.save(os.path.join(os.path.abspath(""), "models", "lr_y_test_pred.npy"), y_test_pred)
        return

    def predict_model_perc(self):
        model = pickle.load(open(os.path.join(os.path.abspath(""), "models", "model_perc.sav"), "rb"))
        y_test_pred = model.predict(self._X_test)
        self._model_perc_acc = self.get_accuracy(y_test_pred)
        self._model_perc_f1 = self.get_f1_score(y_test_pred)
        np.save(os.path.join(os.path.abspath(""), "models", "perc_y_test_pred.npy"), y_test_pred)
        return

    def predict_model_tree(self):
        model = pickle.load(open(os.path.join(os.path.abspath(""), "models", "model_xgbo.sav"), "rb"))
        y_test_pred = model.predict(self._X_test)
        self._model_tree_acc = self.get_accuracy(y_test_pred)
        self._model_tree_f1 = self.get_f1_score(y_test_pred)
        np.save(os.path.join(os.path.abspath(""), "models", "xgbo_y_test_pred.npy"), y_test_pred)
        return

    def get_model_accuracy(self):
        self.predict_model_lr()
        self.predict_model_perc()
        self.predict_model_tree()
        model_acc = pd.DataFrame.from_dict({"Accuracy":[self._model_lr_acc, self._model_perc_acc, self._model_tree_acc],
                                            "Micro-f1":[self._model_lr_f1[1], self._model_perc_f1[1], self._model_tree_f1[1]],
                                            "Macro-f1":[self._model_lr_f1[0], self._model_perc_f1[0], self._model_tree_f1[0]]})
        model_acc.index = ["logistic regression", "perceptron", "xgboost"]
        model_acc.to_hdf(os.path.join(os.path.abspath(""), "models", "model_acc_summary.h5"), key="df", mode="w", format="t")
        return model_acc

if __name__ == "__main__":
    df = pd.read_hdf(os.path.join(os.path.abspath(""), "data", "processed", "covid_data.h5"))
    X_train, X_test, y_train, y_test = data_splitting(df)
    prediction = Prediction(X_test, y_test)
    model_acc = prediction.get_model_accuracy()
    print(model_acc)
