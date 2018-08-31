STEP ONE:
Make sure you have Python 3.6 or greater installed in an virtualenv. Then run
this command from the command prompt:

    pip install -r requirements.txt

This will install all project dependencies.

STEP TWO:
Make and apply migrations:
    python manage.py makemigrations
    python manage.py migrate

STEP THREE:
begin server:
    python manage.py runserver




