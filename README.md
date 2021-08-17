# Question1

## A simple Django application and add a couple of management commands.

<Question1 subfolder :>  is the actual python package for the project

<wfp folder :> is the python application.

<requirements.txt :> is a file containing all the technical requirements for the application

management-> commands : include all the management commands

#### How to run the application
python manage .py runserver 

 - launches the application at localhost: 8000

#### working with the management commands

1. python manage.py countrygen -c 1

    - generates 32 countries with their corresponding interventions

2. python manage.py countryiso iso_code

    - renames the associated intervention code.


