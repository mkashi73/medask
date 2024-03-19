import os
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'medask.settings')
import django
django.setup()
from django.utils import timezone
from api.models import User, Role, Permission


def populate():
    permissions = Permission.objects.all()

    role = None
    try:
        role = Role.objects.get(code_name='su')
        role.permissions.clear()
    except Role.DoesNotExist:
        role = Role.objects.create(name='SuperUser', code_name='su')

    role.permissions.add(*permissions)
    role.save()


    try:
        user = User.objects.get(username='superuser')
    except User.DoesNotExist:
        user = User.objects.create_superuser(
            id=1,
            username="superuser",
            password="C!$@well123",
        )
        user.role = Role.objects.get(code_name='su')
        user.save()

   
if __name__ == '__main__':
    print("Populating medask...")
    populate()