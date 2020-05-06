# Babytron API

Babies/Events management system made with Django implementing JWT auth

## Installation
First install virtualenv
```bash
pip install virtualenv
```

Navigate to the folder where you downloaded the project, then to the folder WEB-LAB4-babytronapi and run:
```bash
> python -m venv myvenv
```
Activate the virtual enviroment
```bash
> myvenv\Scripts\activate.bat
```

Install all dependencies for the project

```bash
pip install -r requirements.txt
```

Run server, default port is localhost:8000
```bash
python manage.py runserver
```

Sample data is already in the database, you can see whats in the database with the initialize.py file

## Data Breakdown

Heres a guide to all the data thats already in the database, you might find this useful to make the http requests in Postman

*  Parent Jorge (id: 3, username: jorge, password: jorge1357)
   * Baby Lisa Perez (id: 8)
   
        * Event (id:8, type: POOP)
          
 
*  Parent Adrian (id: 4,  username: adrian, password: adrian1357)
   * Baby Sara Sanchez (id: 7)
   
        * Event (id: 9, type: FEED)
        * Event (id: 10, type: POOP)
          
      

## License
[MIT](https://choosealicense.com/licenses/mit/)
