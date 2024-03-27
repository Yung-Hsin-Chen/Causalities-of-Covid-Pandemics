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
Topic: Causalities of Covid Pandemics on Countries

## Homework
### Week 1

This task is about command line. commandline-cheatsheet.txt shows some common commands that can be used uder certain scenarios.

runner.sh is a bash script that prints out the string input by user.
 
cron_job.txt describes the steps to run runner.sh everysecond day at 17:00. 

Follow [this](https://github.com/ipozdeev/it-skills-for-research/blob/master/command-line.md) for more task details.

### Week 2

A folder created by cookiecutter Data Science structure is named as final_project in this repo.

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

Follow [this](https://github.com/ipozdeev/it-skills-for-research/blob/master/project-environment.md) and [this](https://github.com/ipozdeev/it-skills-for-research/blob/master/coding-environment.md) for more task details.

### Week 3

The task is done with one person commits. Follow [this](https://github.com/ipozdeev/it-skills-for-research/blob/master/version-control.md) for more task details.

### Week 4

Week 4 is about github coolaboration. Tasks are committed to `test-alice` branch and a pull request to `master` branch is submitted and accepted. Follow [this](https://github.com/ipozdeev/it-skills-for-research/blob/master/collaboration-tools.md) for more task details.

### Week 5

The file generate_data.py is used to generate a large file with gzip, h5 and feather extensions. data.feather file is tracked via git lfs and pushed to origin/midterm. 

The file time_used.txt noted down the time used to generate the three data files. Follow [this](https://github.com/ipozdeev/it-skills-for-research/blob/master/data-management.md) for more task details.

## Reference
