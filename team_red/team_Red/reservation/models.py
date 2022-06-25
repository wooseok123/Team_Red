from django.db import models
from datetime import datetime

# Create your models here.
class Reservation(models.Model):
    start_date = models.DateTimeField(default=datetime.now()) # 예약한 날짜
    end_date = models.DateField() # 예약된 날짜
    num_people = models.IntegerField(default=1) # 예약 인원
    place = models.CharField(max_length=30) # 예약 장소
