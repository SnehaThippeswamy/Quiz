from django.contrib import admin
from .models import QuizType,Question,Score
# Register your models here.

admin.site.register(QuizType)
admin.site.register(Question)
admin.site.register(Score)
