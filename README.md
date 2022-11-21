# Causalities of Covid Pandemics
## Digital Tools for Finance Final Project

## Table of contents
* [Run Files](#run-files)

## Run Files
1. Navigate to ```final_project/```.
2. Build a docker image.
    ```
    docker build -t dtff_final/src:v.1.0 . -f Dockerfile
    ```
3. Run the container in an interactive mode.

    a. Run ```upstream.py``` to load the data from external repository to local database ```data/external```.
    ```
    docker run -it -v $PWD/data/external:/app/data/external dtff_final/src:v.1.0 python datafeed/upstream.py
    ```
    b. Run ```src/build_features.py``` to build features for the models and save it in local database ```data/processed```.
    ```
    docker run -it -v $PWD/data/processed:/app/data/processed dtff_final/src:v.1.0 python src/features/build_features.py
    ```
    c. Train the models with ```src/models/train_model.py```
    ```
    docker run -it -v $PWD/models:/app/models dtff_final/src:v.1.0 python src/models/train_model.py
    ```
    d. Predict with the models with ```src/models/predict_model.py``` and save the predicted label and model accuracy summary table in ```models```.
    ```
    docker run -it -v $PWD/models:/app/models dtff_final/src:v.1.0 python src/models/predict_model.py
    ```
    e. Get feature importance table with ```src/feature_importance/get_geature_importance.py``` and save the feature importance table in ```models```.
    ```
    docker run -it -v $PWD/models:/app/models dtff_final/src:v.1.0 python src/feature_importance/get_feature_importance.py
    ```
