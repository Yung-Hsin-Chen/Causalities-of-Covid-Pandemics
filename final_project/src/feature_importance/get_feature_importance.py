from inspect import modulesbyfile
import os
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
        model_acc = pd.read_hdf(os.path.join(os.path.abspath(""), "models", "model_acc_summary.h5"))
        self._best_model = str(model_acc.idxmax(axis=1)[0])
        model = pickle.load(open(os.path.join(os.path.abspath(""), "models", "model_"+self._best_model[:4]+".sav"), "rb"))
        return model

    def get_importance_table(self):
        model = self.get_best_model()
        importances = pd.DataFrame(data={
            "Feature": pickle.load(open(os.path.join(os.path.abspath(""), "models", "feature_list.pkl"), "rb")),
            "Importance": model.coef_[0]
        })
        importances = importances.sort_values(by="Importance", ascending=False)
        importances.index = np.arange(1, len(importances ) + 1)
        importances.to_hdf(os.path.join(os.path.abspath(""), "models", "feature_importance.h5"), key="df", mode="w", format="t")
        return importances

if __name__ == "__main__":
    feature_importance = FeatureImportance()
    importances = feature_importance.get_importance_table()
    print(importances)