from django.db import models

class OTPModel(models.Model):
    otp = models.IntegerField()
