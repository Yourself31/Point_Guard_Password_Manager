from django.db import models
from django.contrib.auth.models import User

class PasswordCategory(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_categories')

    def __str__(self):
        return self.name

class UserPassword(models.Model):
    category = models.ForeignKey(PasswordCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='passwords')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_passwords')
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True)
    # WARNING: Storing passwords in plaintext is highly insecure.
    # This field should instead store an encrypted password and be decrypted only when necessary.
    password = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.website} - {self.username}"
