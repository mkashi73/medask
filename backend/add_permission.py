import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'medask.settings')

import django
django.setup()

from api.models import Permission

permissions = [
    Permission(name='Create User', code_name='create_user', module_name='User', description='User can create user'),
    Permission(name='Read User', code_name='read_user', module_name='User', description='User can read user'),
    Permission(name='Update User', code_name='update_user', module_name='User', description='User can update user'),
    Permission(name='Show User', code_name='show_user', module_name='User', description='User can view user'),

    Permission(name='Create Role', code_name='create_role', module_name='Role', description='User can create role'),
    Permission(name='Read Role', code_name='read_role', module_name='Role', description='User can read role'),
    Permission(name='Update Role', code_name='update_role', module_name='Role', description='User can update role'),
    Permission(name='Delete Role', code_name='delete_role', module_name='Role', description='User can delete role'),
    Permission(name='Show Role', code_name='show_role', module_name='Role', description='User can view role'),
]


def add_permission():
    for permission in permissions:
        try:
            Permission.objects.get(code_name=permission.code_name)
        except Permission.DoesNotExist:
            permission.save()


if __name__ == '__main__':
    print("Adding permissions...")
    add_permission()
    print("permissions Added...")
