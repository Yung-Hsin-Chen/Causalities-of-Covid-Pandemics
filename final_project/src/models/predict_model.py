import os
import sys
parentdir = os.path.dirname("final_project")
sys.path.insert(0, parentdir)
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from sklearn.metrics import confusion_matrix
from src.models.data_splitting import data_splitting


class Prediction:

    def __init__(self, X_train, X_test, y_train, y_test):
        self._X_train = X_train
        self._X_test = X_test
        self._y_train = y_train
        self._y_test = y_test

    def 
        