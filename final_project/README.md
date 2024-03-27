# Causalities of Covid Pandemics
## Digital Tools for Finance Final Project

## Table of contents
* [Run Files](#run-files)
* [Run Jupyter Notebook for Visualisation](#run-jupyter-notebook-for-visualisation)
* [Compile the Report](#compile-the-report)
* [Compile the Presentation](#compile-the-presentation)

Welcome everyone! This repository allows you to play around with the covid pandemic data. It aims to get the most influenced causalities of the pandemic. Find out more about how we did it in the report and presentation located in ```final_project/reports/``` folder!

By following the instructions below, you can download and clean your own data and train it by the provided three models. The results and data will be saved to the notebook, where you can explore more.  

## Run Files
1. Navigate to ```final_project/```.
2. Build a docker image.
    ```
    docker build -t dtff_project/covid:v.1.0 . -f Dockerfile
    ```
3. Run the container in an interactive mode.

    1. Run ```upstream.py``` to load the data from external repository to local database ```data/external```.
        ```
        docker run -it -v $PWD/data/external:/app/data/external dtff_project/covid:v.1.0 python src/datafeed/upstream.py
        ```
    2. Run ```src/build_features.py``` to build features for the models and save it in local database ```data/processed```.
        ```
        docker run -it -v $PWD/data/processed:/app/data/processed dtff_project/covid:v.1.0 python src/features/build_features.py
        ```
    3. Train, predict the models and get feature_importances with ```src/main.py```. This will take a bit more than 10 minutes. 
        ```
        docker run -it -v $PWD/models:/app/models dtff_project/covid:v.1.0 python src/main.py
        ```

## Run Jupyter Notebook for Visualisation
1. Navigate to ```final_project/```.
2. Run the following command in a terminal. This will save the notebooks locally and show the existing notebook in the docker container. All results will be loaded into the notebook automatically. Just enter the notebook directory in the container, find the ```visualize_EDA.ipynb``` and have fun with your own visualisations.
    ```
    docker run -p 8888:8888 --name notebook --rm -v $PWD/src/visualization:/home/jovyan/notebook -v $PWD/data/external:/home/jovyan/data/external -v $PWD/data/processed:/home/jovyan/data/processed -v $PWD/models:/home/jovyan/models -e JUPYTER_ENABLE_LAB=yes jupyter/datascience-notebook
    ```

## Compile the Report

1. Navigate to ```final_project/```.
2. Build the docker container.
    ```
    docker build -t dtff_project/covid_report:v.1.0 . -f reports/Dockerfile
    ```
3. Run the docker container.
    ```
    docker run -it -v $PWD/reports/report:/work/reports/report dtff_project/covid_report:v.1.0
    ```
4. After getting inside the docker container, navigate to ```reports/report```.
    ```
    cd reports/report
    ```
5. Compile the ```report.tex```.
    ```
    pdflatex report
    ```

## Compile the Presentation

1. Navigate to ```final_project/```.
2. Build the docker container (the same container as the report one).
    ```
    docker build -t dtff_project/covid_report:v.1.0 . -f reports/Dockerfile
    ```
3. Run the docker container.
    ```
    docker run -it -v $PWD/reports/presentation:/work/reports/presentation dtff_project/covid_report:v.1.0
    ```
4. After getting inside the docker container, navigate to ```reports/report```.
    ```
    cd reports/presentation
    ```
5. Compile the ```report.tex```.
    ```
    pdflatex presentation
    ```
