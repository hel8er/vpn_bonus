from django.db import models
# Create your models here.


class TgUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.SlugField(null=True, blank=True)
    join_date = models.DateField(auto_now=True, null=True, blank=True)
    joined_by = models.ForeignKey('self', null=True, blank=True, related_name='refs', on_delete=models.SET_NULL)
    payment_exp = models.DateField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
