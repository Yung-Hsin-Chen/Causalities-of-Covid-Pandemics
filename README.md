# Causalities of Covid Pandemics

## Table of contents
* [Run Files](#run-files)
* [Run Jupyter Notebook for Visualisation](#run-jupyter-notebook-for-visualisation)
* [Compile the Report](#compile-the-report)
* [Compile the Presentation](#compile-the-presentation)

## Run Files
1. Navigate to ```final_project/```.
2. Build a docker image.
    ```
    docker build -t dtff_project/covid:v.1.0 . -f Dockerfile
    ```
3. Run the container in an interactive mode.

    1. Run ```upstream.py``` to load the data from external repository to local database ```data/external```.
        ```
        docker run -it -v $PWD/data/external:/app/data/external dtff_project/covid:v.1.0 python datafeed/upstream.py
        ```
    2. Run ```src/build_features.py``` to build features for the models and save it in local database ```data/processed```.
        ```
        docker run -it -v $PWD/data/processed:/app/data/processed dtff_project/covid:v.1.0 python src/features/build_features.py
        ```
    3. Train the models with ```src/models/train_model.py```
        ```
        docker run -it -v $PWD/models:/app/models dtff_project/covid:v.1.0 python src/models/train_model.py
        ```
    4. Predict with the models with ```src/models/predict_model.py``` and save the predicted label and model accuracy summary table in ```models```.
        ```
        docker run -it -v $PWD/models:/app/models dtff_project/covid:v.1.0 python src/models/predict_model.py
        ```
    5. Get feature importance table with ```src/feature_importance/get_geature_importance.py``` and save the feature importance table in ```models```.
        ```
        docker run -it -v $PWD/models:/app/models dtff_project/covid:v.1.0 python src/feature_importance/get_feature_importance.py
        ```

## Run Jupyter Notebook for Visualisation
1. Navigate to ```final_project/```.
2. Run the following command in a terminal. This will save the notebooks locally and show the existing notebook in the docker container.
    ```
    docker run -p 8888:8888 --name notebook -v $PWD/src/visualization:/home/dtff/covid -e JUPYTER_ENABLE_LAB=yes --env-file .env -it jupyter/datascience-notebook
    ```
3. After finished using the jupyter notebook, the container can be removed by the following command.
    ```
    docker rm <container-id>
    ```
    The ```<container-id>```can be checked with 
    ```
    docker ps -a
    ```

## Compile the Report

1. Navigate to ```final_project/```.
2. Build the docker container.
    ```
    docker build -t dtff_project/covid_report:v.1.0 . -f reports/Dockerfile
    ```
3. Run the docker container.
    ```
    docker run -it -v $PWD/reports/report:/work/reports/report dtff_project/covid_report:v.1.1
    ```
4. After getting inside the docker container, navigate to ```reports/report```.
    ```
    cd reports/report
    ```
5. Compile the ```report.tex```.
    ```
    pdflatex report.tex
    ```

## Compile the Presentation

1. Navigate to ```final_project/```.
2. Build the docker container.
    ```
    docker build -t dtff_project/covid_report:v.1.0 . -f reports/Dockerfile
    ```
3. Run the docker container.
    ```
    docker run -it -v $PWD/reports/report:/work/reports/report dtff_project/covid_report:v.1.1
    ```
4. After getting inside the docker container, navigate to ```reports/report```.
    ```
    cd reports/report
    ```
5. Compile the ```report.tex```.
    ```
    pdflatex report.tex
