# Django + Type Hints

A playground for Django + Type Hints 

See:
- https://github.com/typeddjango/django-stubs
- https://github.com/microsoft/pylance-release/issues/14

## Getting Started
```shell
# Clone repo
git clone https://github.com/joeriddles/test_django_stubs.git

# Create virtual environment
cd test_django_stubs
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
cd test_stubs
python manage.py migrate

# Start Django server
python manage.py runserver
```
