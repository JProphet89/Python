from django.db import models


class Biker(models.Model):
    name = models.CharField(max_length=40)
    phone = models.IntegerField(max_length=10)
    start_time = models.TimeField(default='00:00:00', auto_now_add=False, auto_created=False)
    first_check = models.TimeField(auto_now_add=False, auto_created=False, default='00:00:00')
    second_check = models.TimeField(auto_now_add=False, auto_created=False, default='00:00:00')
    final_check = models.TimeField(auto_now_add=False, auto_created=False, default='00:00:00')

    def __unicode__(self):
        return self