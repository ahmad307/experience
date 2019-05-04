# Experience
A web paltform for sharing unique experiences you have had.

If you are facing a challenge, trying to deal with a severe problem or moving to a new city. Experience is the place to find stories by people who were once in your shoes and successfully dealt with/defeated that challenge.

## Built With
- Django
- MongoDB
- Pymongo


## Installation
- Make sure you have Python 3.x installed in your environment.
- It's recommended to create a virtual environment by running ```pip install virtualenv``` and then running ```virtualenv env``` in the main directory.
- Run the virutal environment using:
    - On windows ```.\env\Scripts\actiavate```
    - On Linux ```source env/bin/activate```
- Install the needed packages by running ```pip install requirements.txt```
- Navigate to ```/stories/models.py``` and change the address and the port on line 4 to conform to your local MongoDB address. The defaults will usually be fine.
- To start the server run ```python manage.py runserver```
On windows you can also try ```py manage.py runserver```