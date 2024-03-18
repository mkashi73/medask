from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid


def get_profile_image_path(self, filename):
    return f'profile_images/users/{self.pk}/{str(uuid.uuid4())}.png'


def get_default_profile_image_path():
    return f'profile_images/{"default_profile_image.png"}'


class UserManager(BaseUserManager):
    def create_user(self, id, username, password=None):
        if not username:
            raise ValueError('User must have a username.')
        user = self.model(
            id=id,
            username=username,
        )
        user.staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, username, password):
        user = self.create_user(
            id=id,
            username=username,
            password=password
        )
        # user.is_staff = True
        user.superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    center = models.ForeignKey('Center', null=True, on_delete=models.SET_NULL, related_name='+')
    name = models.CharField(max_length=255, blank=True, null=True)
    profile_status = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    svc_number = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.CharField(max_length=255, blank=True, null=True)
    rank_name = models.CharField(max_length=255, blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    rank_order = models.BigIntegerField(blank=True, null=True)
    rank_id = models.BigIntegerField(blank=True, null=True)
    appointment_id = models.BigIntegerField(blank=True, null=True)
    appointment_name = models.CharField(max_length=255, blank=True, null=True)
    appointment_order = models.BigIntegerField(blank=True, null=True)
    executive_order = models.BigIntegerField(blank=True, null=True)
    appointment_type = models.CharField(max_length=255, blank=True, null=True)
    data_center_id = models.BigIntegerField(blank=True, null=True)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_path, null=True, blank=True,
                                      default=get_default_profile_image_path)

    role = models.ForeignKey('Role', related_name='users', blank=True, null=True, on_delete=models.CASCADE)
    

    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.superuser
    @property 
    def is_superuser(self):
        return self.superuser