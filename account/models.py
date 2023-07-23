from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **kwargs):
        if not username:
            return ValueError('No username')
        elif not email:
            return ValueError('Email was not handed')
        email = self.normalize_email(email=email)
        user = self.model(email=email, username=username, **kwargs)
        user.create_activation_code()
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **kwargs)

    def create_superuser(self, username, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('SuperUser must be a staff, currently not!')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('SuperUser must be a superuser, currently not!')
        return self._create_user(username, email, password, **kwargs)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    activation_code = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(
        default=False, help_text='This field is for user activation'
    )
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def create_activation_code(self):
        import uuid

        code = str(uuid.uuid4())
        self.activation_code = code


# class Contact(models.Model):
#     contact1 = models.ForeignKey(CustomUser, related_name='my_contacts',on_delete=models.CASCADE)
#     contact2 = models.ForeignKey(CustomUser, related_name='contacts', on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ['contact1', 'contact2']
#
#     def __str__(self):
#         return f'{self.contact1.username} -> {self.contact2.usernafme}'

class Contact(models.Model):
    contact1 = models.ForeignKey(CustomUser, related_name='my_contacts',on_delete=models.CASCADE)
    contact2 = models.ForeignKey(CustomUser, related_name='contact', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['contact1', 'contact2']

    def __str__(self):
        return f'{self.contact1.username} -> {self.contact2.username}'