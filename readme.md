# Fanlytiks!

Realtime twitter analysis of the hashtag #VIVOIPL. The project is hosted at: [https://internship.milanmenezes.me/fanlytiks](https://internship.milanmenezes.me/fanlytiks)

## Installation
You can install python-twitter using:

    git clone https://github.com/milanmenezes/fanlytiks.git

## Requirements

 - python-twitter
 - psycopg2
 - flask

The requirements can be installed using:

    pip install -r requirements.txt

## Files

The project contains the following files:

     - fanlytiks.py
     - reverseupdate.py
     - forwardupdate.py

The functionality of each file is listed below
## fanlytiks
The `fanlytiks.py` file is the flask file which is used to run the server. 

> The `fanlytiks.wsgi` is the mod-wsgi file used to run the server
> behind apache server.

## reverseupdate
The `reverseupdate.py` file is used to call the twitter api to get the tweets iteratively in reverse direction and store the required values in the database.

## forwardupdate
The `forwardupdate.py` file is used to call the twitter api to get the recent tweets iteratively and store the required values in the database.

> The `forwardupdate.py` can be added as a cronjob to be executed
> repeatedly at given intervals of time.