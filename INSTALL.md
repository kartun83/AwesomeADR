# Install dependencies
pip install django-crispy-forms
pip install django-tables2

# Perform migration
CD to top level directory
python manage.py makemigrations
If previous runs without errors make tables in DB
python manage.py migrate

Test it: 
python manage.py runserver