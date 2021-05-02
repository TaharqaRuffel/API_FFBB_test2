from django.db import models

# Create your models here.
class Match(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    championship = models.CharField(max_length=100)
    day = models.IntegerField()
    match_date = models.DateTimeField()
    home = models.CharField(max_length=100)
    visitor = models.CharField(max_length=100)
    score_home = models.SmallIntegerField(default=0)
    score_visitor = models.SmallIntegerField(default=0)
    plan = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['created']