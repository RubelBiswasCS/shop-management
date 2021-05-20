##Super Shop Management System

This is a super shop management system with basic functionalities, like managing products and orders. For this project Python is used with Django framework and for database management used SQLite.

#Installation

For installing this project, Virtual Environment is recommended. So lets setup the virtual environment,
Open your Terminal and run this command:
    '''
    sudo apt-get python3
    mkdir Django_Project
    cd Django_Project
    sudo apt-get install python3-venv
    python3 -m venv myvenv
    source myvenv/bin/activate
    '''
Now virtual environment is activated, its time for cloneing the project. for this run this command bellow,
    '''
    git clone https://github.com/RubelBiswasCS/shop-management
    '''
Now cd into the project directory
    '''
    cd shop-management
    '''
Install dependencies,
    '''
    pip install --upgrade pip
    pip install -r requirements.txt
    '''
at this point the requirment up-to-date.lets do the migrations by runnning those command
    '''
    python manage.py makemigrations
    python manage.py migrate
    '''
As migration done, lets create a superuser for this application. For doing so run the commend down bellow and give proper credentials as required.
    '''
    python manage.py createsuperuser
    '''
Now you can run this application by running
    '''
    python manage.py runserver
    '''






