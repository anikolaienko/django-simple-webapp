from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Poll(models.Model):
    title = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    order_id = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        True if question was publication date is not older than 24 hours from now
        and not in the future.
        """
        now = timezone.now()
        return now - timedelta(days=1) <= self.created_at < now
    was_published_recently.admin_order_field = 'created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Created recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text