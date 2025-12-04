from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models.time_stamp import TimeStampModel
# Create your models here.
class CustomUser(TimeStampModel , AbstractUser):

  DEPARTMENT_CHOICES = {
    ('CSE' , 'Computer Science and Engineering'),
    ('EEE' , 'Electrical and Electronics Engineering'),
    ('BBA' , 'Bachelor of Business Administration'),
    ('ENG' , 'English'),
    ('LAW' , 'Law'),
    ('ARCH' , 'Architecture'),
  }
  phone = models.CharField(max_length=15)
  image = models.ImageField(upload_to='Student_ID/' , null=True , blank=True)
  institute = models.CharField(null=True , blank=True)
  department = models.CharField(
    choices=DEPARTMENT_CHOICES,
    null=True,
    blank=True,
    default=None

  )

  def __str__(self):
    return f"{self.email} -- {self.institute}"
