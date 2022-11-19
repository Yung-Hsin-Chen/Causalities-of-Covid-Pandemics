import os
import sys
parentdir = os.path.dirname("final_project")
sys.path.insert(0, parentdir)
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from sklearn.metrics import confusion_matrix
from src.models.data_splitting import data_splitting
import pickle
import pandas as pd


class Prediction:

    def __init__(self, X_test, y_test):
        self._X_test = X_test
        self._y_test = y_test
        self._model_lr_acc = 0
        self._model_perc_acc = 0
        self._model_tree_acc = 0

    def get_accuracy(self, y_test, y_test_pred):
        correct = 0

        for i, v in enumerate(list(y_test)):
            if v == y_test_pred[i]:
                correct += 1
        return correct/len(y_test)

    def predict_model_lr(self):
        model = pickle.load(open(os.path.join(os.path.abspath(""), "models", "model_lr.sav"), "rb"))
        y_test_pred = model.predict(self._X_test)
        self._model_lr_acc = self.get_accuracy(self._y_test, y_test_pred)
        return

    def predict_model_perc(self):
        model = pickle.load(open(os.path.join(os.path.abspath(""), "models", "model_perc.sav"), "rb"))
        y_test_pred = model.predict(self._X_test)
        self._model_lr_acc = self.get_accuracy(self._y_test, y_test_pred)
        return

    def predict_model_tree(self):
        model = pickle.load(open(os.path.join(os.path.abspath(""), "models", "model_tree.sav"), "rb"))
        y_test_pred = model.predict(self._X_test)
        self._model_lr_acc = self.get_accuracy(self._y_test, y_test_pred)
        return

    def get_model_accuracy(self):
        self.predict_model_lr()
        self.predict_model_perc()
        self.predict_model_tree()
        model_acc = pd.DataFrame.from_dict({"logistic regression":self._model_lr_acc,
                                            "perceptron":self._model_perc_acc,
                                            "decision tree":self._model_tree_acc})
        return model_acc
