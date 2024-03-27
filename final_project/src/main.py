import os
from dotenv import dotenv_values
PYTHONPATH = dotenv_values(".env")["PYTHONPATH"]
import sys
parentdir = os.path.dirname("final_project")
sys.path.insert(0, parentdir)
from src.models.train_model import train
from src.models.predict_model import predict
from src.feature_importance.get_feature_importance import feature_importance

if __name__ == "__main__":
    train()
    predict()
    feature_importance()
