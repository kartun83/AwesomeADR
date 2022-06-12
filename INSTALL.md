# Install dependencies
```
pip install django-crispy-forms
pip install django-tables2
pip install requests
```


# Perform migration
CD to top level directory
```
python manage.py makemigrations
```
If previous runs without errors make tables in DB
```
python manage.py migrate
```

# Create superuser
```
python manage.py createsuperuser
```

# Test it
```
python manage.py runserver
```
By default it starts webservice on 127.0.0.1:8000

# Prefill some required data
using admin UI [127.0.0.1:8000/admin] fill: 
- Systems table. It's suggested to add entry for ALL to simplify maintanence
- Influences table. Suggested: Causes, Viloates, Cancels, Extends
- Statuss table. Proposed, Alternative, Temporary, Superseeded/cancelled, Active