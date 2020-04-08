from django.conf import settings
from django.db import models
from django.utils import timezone

class UseDemand(models.Model):
    name = models.CharField('대표 학생', max_length=10)
    place = models.CharField('위치', max_length=15)
    num_people = models.IntegerField(default=1)
    purpose = models.TextField()
    demand_time= models.DateTimeField(
        auto_now=True # 최종 저장된 시간으로 자동저장
    )
    start_time = models.DateTimeField(
        default=timezone.now # 값이 지정되지 않았을 때 사용하는 값
    )
    finish_time = models.DateTimeField(blank=False, null=False)



# https://tutorial.djangogirls.org/ko/django_admin/
