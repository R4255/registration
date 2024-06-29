## Installation Guide

### Clone the Repository
1. Open your terminal or command prompt.
2. Change the current working directory to the location where you want the cloned directory.
3. Type the following command:
      ```sh
      git clone https://github.com/R4255/registration.git
      ```
     cd registration
     ```
     python -m venv env
     ```
     .\env\Scripts\activate
     ```
     pip install -r requirements.txt
     ```
     python manage.py makemigrations
     ```
     python manage.py migrate
     ```
     python manage.py createsuperuser
     ```
     python manage.py runserver
