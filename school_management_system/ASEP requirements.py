'''Install pqSQL version 15
Remove virtualenvwrapper from requirements
Change pillow version to 9.4.0 in requirments.txt
#To Run the files
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
user ID : amrutha
Password: adminpassword'''


