from django.db import models
from django.contrib.auth.models import User

class QuizType(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	create_date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.name

class Question(models.Model):
	id = models.AutoField(primary_key=True)
	quiz = models.ForeignKey(QuizType, on_delete=models.CASCADE)
	question = models.TextField()
	option_1 = models.TextField()
	option_2 = models.TextField()
	option_3 = models.TextField()
	option_4 = models.TextField()
	answer = models.CharField(max_length=1)
	marks = models.IntegerField()
	create_date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.question

class Score(models.Model):
	id=models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answered = models.CharField(max_length=1)
	is_correct = models.BooleanField(default=False)
	score = models.IntegerField()
	answered_date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.user + self.question