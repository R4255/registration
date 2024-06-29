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
  ```sh
  .\env\Scripts\activate
  ```sh
  pip install -r requirements.txt
  ```sh
  python manage.py makemigrations
  ```sh
  python manage.py migrate
  ```sh
  python manage.py createsuperuser
  ```sh
  python manage.py runserver
