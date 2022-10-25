# Digital Tools for Finance

## Table of contents
* [Final Project](#final-project)
* [Homework](#homework)
    * [Week 1](#week-1)
    * [Week 2](#week-2)
    * [Week 3](#week-3)
    * [Week 4](#week-4)
    * [Week 5](#week-5)
* [Reference](#reference)

## Final Project

## Homework
### Week 1
### Week 2

The file, plot.py, creates a pie chart of Pringles Original Chips nutritions from the data in ./data/coding-environment-exercise.csv. A docker file is provided so that no additional dependencies are needed to install. Please follow the steps below to plot the figure yourself (assuming dockers are installed).

1. Navigate to week_2 folder.
2. Build the image by the following command:
    ```
    docker build -t dtff/plot-pringles:v.1.1 .
    ```
3. Run the container with the following command:
    ```
    docker run -it -v $PWD/result:/app/result dtff/plot-pringles:v.1.1 python plot.py
    ```
4. Find the plot in the ./result/ folder locally.

### Week 3
### Week 4
### Week 5

The file generate_data.py is used to generate a large file with gzip, h5 and feather extensions. data.feather file is tracked via git lfs and pushed to origin/midterm.

The file time_used.txt noted down the time used to generate the three data files.

## Reference
