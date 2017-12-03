# django-rest-quickstart

A Django REST quickstart project with a simple RBAC / ACL example.

# Requirements

- docker >= 17.11

# Set up

`$ docker-compose run web python manage.py migrate`

If you receive an error like "could not connect to server: Connection refused", re-run the command.

Create some users

`$ docker-compose run web python manage.py shell`

```
from django.contrib.auth.models import User
u1 = User.objects.create_user(username='user1', password='hello', is_staff=True, first_name='foo', last_name='bar')
u2 = User.objects.create_user(username='user2', password='world', is_staff=True, first_name='baz', last_name='xyz')
```
# Run

`$ docker-compose up`

# Test

`curl -H "Authorization: Basic dXNlcjE6aGVsbG8=" http://0.0.0.0:8000/api/profiles/ -v`

("dXNlcjE6aGVsbG8="" is "user1:hello" base64-encoded)

You should only be able to see 1 user profile - the one belonging to 'user1'.
