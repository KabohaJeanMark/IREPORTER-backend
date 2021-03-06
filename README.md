# iREPORTER

[![Build Status](https://travis-ci.com/KabohaJeanMark/IREPORTER-CHALLENGE-3.svg?branch=develop)](https://travis-ci.com/KabohaJeanMark/IREPORTER-CHALLENGE-3) [![Coverage Status](https://coveralls.io/repos/github/KabohaJeanMark/IREPORTER-CHALLENGE-3/badge.svg?branch=ch-feedback-163456258)](https://coveralls.io/github/KabohaJeanMark/IREPORTER-CHALLENGE-3?branch=ch-feedback-163456258) [![Maintainability](https://api.codeclimate.com/v1/badges/34cd9b3182e2be45386e/maintainability)](https://codeclimate.com/github/KabohaJeanMark/IREPORTER-CHALLENGE-3/maintainability)

## About
iReporter gives all citizens a platfrom to raise concerns about corruption and corruption red-flag cases and the need for government intervention in situations.


## Features
1. Users can sign up.
2. Users can create incidents (red-flag records or intervention records)
3. Users can edit the locations and comments of their incidents.
4. Users can delete their incidents.
5. Administrators can update the statuses of these incidents. 

## Prerequisites
- A computer with an OS running python 3.6
- Gitbash installed to navigate between the branches.
- A preferred text editor for example VS Code.
- Postman to locally check the API endpoints acting as your application client. 
- Pytest, nosetest or a preferred python testing tool.

## How to install and deploy
Clone this project to your computer on yourFolder by typing these commands in the terminal.
```
$ mkdir yourFolder
$ cd yourFolder
$ git clone https://github.com/KabohaJeanMark/IREPORTER-CHALLENGE-3
$ cd IREPORTER-CHALLENGE-3
$ virtualenv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ python run.py
```
## Test your endpoints
Run the command in your virtual environment
```
$ pytest
```
## Deployment
The application is hosted on Heroku at https://kjmkireporter.herokuapp.com/api/v1/

## Endpoints
|HTTP Header   | Endpoints                                              | Functionality                               |                             
|--------------| -------------------------------------------------------|:-------------------------------------------:|
|    POST      |```/api/v1/auth/signup```                               |```Registers a user```                       |
|    POST      |```/api/v1/auth/signin```                               |```Signs in a user```                        |
|    POST      |  ```/api/v1/users```                                   |```Create a user```                          |
|    POST      | ```/api/v1/interventions```                            |```Create intervention record```             | 
|    GET       |``` /api/v1/users```                                    |```Fetch all users```                        |
|    GET       |``` /api/v1/interventions```                            |```Fetch all intervention records```         |
|    GET       |``` /api/v1/interventions/<intervention_id>```          |```Fetch a particular intervention record``` |                   
|   DELETE     |``` /api/v1/interventions/<intervention_id>```          |```Delete a specific intervention record```  |
|   PATCH      |``` /api/v1/interventions/<intervention_id>/status  ``` |```Update a specific intervention's status```|
|   PATCH      |```/api/v1/interventions/<intervention_id>/location```  |```Update a specific intervention location```| 
|   PATCH      |```/api/v1/interventions/<intervention_id>/comment```   |```Update a specific intervention comment``` |
|   POST       |```/api/v1/redflags```                                  |```Create redflag record```                  | 
|   GET        |```/api/v1/redflags```                                  |```Fetch all intervention records```         |
|   GET        |```/api/v1/redflags/<redflag_id>```                     |```Fetch a particular redflag record```      | 
|   DELETE     |```/api/v1/redfags/<redflag_id>```                      |```Delete a specific redflags record```      |
|   PATCH      |```/api/v1/redfags/<redflag_id>/status  ```             |```Update a specific redflags status```      |
|   PATCH      |```/api/v1/redfags/<redflag_id>/location```             |```Update a specific redflags location```    | 
|   PATCH      |```/api/v1/redfags/<redflag_id>/comment```              |```Update a specific redflags comment```     | 




## Built using:
- Language : Python
- Framework : Flask
- Database  : Postgresql

## Author
>Kaboha Jean Mark Kairumba.

>email: kabohajeanmark@gmail.com

## Licensing
The is an opensource application. All users are free to edit and improve it. Merge off the develope branch and code away, commiting small changes back into it.

## Appreciation
Thank you ANDELA for the opportunity to learn new skills and improve with this bootcamp.
