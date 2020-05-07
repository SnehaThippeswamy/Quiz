from django.urls import path
from . import views

urlpatterns = [
    path('quiztype/<int:type_id>',views.quiztype,name="quiztype"),
    path('answer/<int:q_id>',views.answer,name="answer"),
]
