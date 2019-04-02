from django.db import models


class User(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=20)
    email = models.EmailField(
        max_length=254, blank=False, unique=True,
        error_messages={'required': 'Please provide your email address.',
                        'unique': 'An account with this email exist.'},)
    web = models.URLField(null=True, blank=True)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
