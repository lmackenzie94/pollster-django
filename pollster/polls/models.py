from django.db import models

# Create your models here.

# Question extends Model


class Question(models.Model):
    # an ID is created automatically
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # link choice to the Question
    # CASCADE says if Question is deleted, delete all the Choices
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
