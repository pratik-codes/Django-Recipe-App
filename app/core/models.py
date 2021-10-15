from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):

     def create_user(self, email, password=None, **extra_fields):
          """ creates a user """
          user = self.model(email=self.normalize_email(email), **extra_fields)
          user.set_password(password)
          user.save(using=self._db)

          return user

     def create_superuser(self, email, password):
          """ Create a new superuser """
          user = self.create_user(email=email, password=password)
          user.is_superuser = True
          user.is_staff = True
          user.save(using=self._db)

          return user
 
class User(AbstractBaseUser, PermissionsMixin):
     """ custom user model that supports using email insted of username """
     email = models.EmailField(max_length=225, unique=True)
     name = models.CharField(max_length=225)
     is_active = models.BooleanField(default=True)
     is_staff = models.BooleanField(default=False)

     objects = UserManager()

     USERNAME_FIELD = 'email'

