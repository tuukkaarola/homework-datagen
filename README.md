# Introduction 
This is a small Python program to create datasets for the Invinite Docker Homework.

# Getting Started

You need to have Python 3.10 or later installed 

Generate the test data set by running

``` python3 datagen.py [num_of_years num_of_entries]``` 

or in Windows:

``` python datagen.py [num_of_years num_of_entries]``` 


You may omit the num_of_years and num_of_entries arguments. In the case, the script will produce 10 years worth of data, 100 000 rows for each year.

You may want to use a smaller dataset while developing the solution. For example:

``` python3 datagen.py 10 10``` 

or in Windows:

``` python datagen.py 10 10``` 


The script will produce two files: *data.csv* and *ref.csv*
