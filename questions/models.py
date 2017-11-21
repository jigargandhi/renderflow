from django.db import models

# Create your models here.


class Question(models.Model):
    question_title = models.CharField(max_length=250, blank=False)
    question_text = models.TextField(blank=False)
    creation_date = models.DateTimeField(auto_now=True)
    score = models.IntegerField()
    tags = models.CharField(max_length=200 )
   

class Answer(models.Model):
    answer_text = models.TextField(blank=False)
    answer_date = models.DateTimeField(auto_now=True)
    answer_score=models.IntegerField()
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
   



class Tag(models.Model):
    tag_name=models.CharField(max_length=20)
    tag_count=models.IntegerField()


