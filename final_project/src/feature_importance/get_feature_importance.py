import os
from dotenv import dotenv_values
PYTHONPATH = dotenv_values(".env")["PYTHONPATH"]
import sys
parentdir = os.path.dirname("final_project")
sys.path.insert(0, parentdir)
import pandas as pd
import pickle
import numpy as np

class FeatureImportance:

    def __init__(self):
        self._model_lst = []
        self._best_model = ""
        # self._model = ""

    def get_best_model(self):
        model_acc = pd.read_hdf(os.path.join(PYTHONPATH, "models", "model_acc_summary.h5"))
        self._best_model = str(model_acc["Accuracy"].idxmax(axis=0))
        model = pickle.load(open(os.path.join(PYTHONPATH, "models", "model_"+self._best_model[:4]+".sav"), "rb"))
        return model

    def get_importance_table(self):
        model = self.get_best_model()   
        if self._best_model == "xgboost":
            importance_score = model.best_estimator_.feature_importances_
        else:
            importance_score = model.coef_[0]   
        importances = pd.DataFrame(data={
            "Feature": pickle.load(open(os.path.join(PYTHONPATH, "models", "feature_list.pkl"), "rb")),
            "Importance": importance_score
        })
        importances = importances.sort_values(by="Importance", ascending=False)
        importances.index = np.arange(1, len(importances ) + 1)
        importances.to_hdf(os.path.join(PYTHONPATH, "models", "feature_importance.h5"), key="df", mode="w", format="t")
        return importances

def feature_importance():
    feature_importance = FeatureImportance()
    importances = feature_importance.get_importance_table()
    print(importances)
    return