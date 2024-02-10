from django.db import models
import hashlib

class UserManager(models.Manager):
    def create_user(self, name, email, password, profile_image):
        # Create a new user instance and save it to the database
        password_hash = User.password_hash(password)
        user = self.create(name=name, email=email, password=password_hash, profile_image=profile_image)
        return user

    def authenticate(self, email, password):
        # Check if the user exists in the database and if the provided password matches
        password_hash = User.password_hash(password)
        try:
            user = self.get(email=email, password=password_hash)
            return user
        except User.DoesNotExist:
            return None

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255,null=True)
    profile_image = models.ImageField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    @staticmethod
    def password_hash(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return self.name
