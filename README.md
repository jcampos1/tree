Step One:
    Make sure you have Python 3.6 or greater installed in an virtualenv. Then run
    this command from the command prompt:

        pip install -r requirements.txt

    This will install all project dependencies.

Step two:
    Make and apply migrations:
        python manage.py makemigrations
        python manage.py migrate

Step Three:
    begin server:
        python manage.py runserver




