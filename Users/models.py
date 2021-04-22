from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def LoginValidator(self, LogData):
        errors = {}
        # Login Error Messages
        # Username error
        if len(LogData['log_username']) < 5 :
            errors['log_username'] = 'Please input a valid Username.'
            # maybe add a validation to see if username exist
        # password error
        if len(LogData['log_password']) < 8:
            errors['log_password'] = 'Password must be at least 8 characters.'
        return errors
    
    def RegistrationValidator(self, RegData):
        errors ={}
        EMAIL_REGEX = re.compile( r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # Registration Error Messages
        # first name error
        if len(RegData['first_name']) < 2 :
            errors['first_name'] = 'First name must be at least 2 characters.'
        # last name error
        if len(RegData['last_name']) < 2 :
            errors['last_name'] = 'Last name must be at least 2 characters.'
        # email error
        if not EMAIL_REGEX.match(RegData['email']):
            errors['email'] = 'Email format is incorrect.'
        # username error
        if len(RegData['username']) < 5:
            errors['username']= 'Username must be at least 5 characters.'
        # password error
        if len(RegData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters.'
        # confirm pw
        if RegData['password'] != RegData['confirm_pw']:
             errors['confirm_pw'] = 'Passwords do not match!!!'


class User (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password =  models.CharField(max_length=70)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)



class Journal_Entires(models.Model):
    entry = models.TextField()
    user = models.ForeignKey(User, related_name='journal_entry', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


class Quotes(models.Model):
    the_quote = models.TextField(null=True)
    quote_author = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, related_name='quote', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
