from django.db import models


class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()

    def __str__(self):
        return f"Answer to: {self.question.text}"
