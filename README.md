# Additional-Task

The framework is based on the page-object model, according to which pages are presented as classes,
and the page-components approach is also used, where the page is divided into components

structure:
app - contains class constants for work with target app.
    pages - contains description for pages in app
        components - most of the functionality is described as a class with a set of fields and a method for convenient interaction with them
            dialog - class for interaction with pop-ups
config-contains configuration for communication with app
test - contains tests scenario and constants
    data - contains some tests file


Regression:
to run the regression, you can run the main.py file
or
run the tests folder

report will generate at report folder
for generate report you need install allure on system and run in console:
"allure serve reports"

----------------------------------------------------------------------------------
|for run in firefox, you need to add the token file from github to the config file|
----------------------------------------------------------------------------------
|For run in multiprocessing use "xdist" lib                                      |
----------------------------------------------------------------------------------