# Unit Testing with Python

![example workflow](https://github.com/StatsGary/unit_testing_with_python/actions/workflows/main.yml/badge.svg)

This repository shows how to use the module `unittest` to create testing. Then I have created a GitHub actions files to check the build for failures. 

The folder structure is defined to have the tests isolated in their own folder. 

## Explaining each component

- Workflows - this contains a YAML file that tests the script runs on various versions of Python and then returns successful if it does. The unit tests are run here, so if any thing breaks in development, then you will be notified. 
- functions - this is a sub directory that has the script to create the calculator functions
- tests - contains the example unit tests to run - one for the employee class and another one for the calculator tests. Best practice to isolate tests in their own file and this can then be referenced by the YAML file

The root of the project contains the employee class and a requirements file for an additional packages that need to be installed, these are specified in the yaml file for running on the virtual testing machines in Linux. 



