from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import QuizType,Question,Score

def home(request):
	quiz = QuizType.objects.all()
	return render(request,"quiz/home.html", {'type':quiz})

@login_required(login_url='account/login')
def quiztype(request, type_id):
	questions = Question.objects.filter(quiz = type_id)
	return render(request,"quiz/type.html", {'questions' : questions})

@login_required(login_url='account/login')
def answer(request, q_id):
	answered = []
	if request.method == "POST":
		answered.append(request.POST.get("option_1","off"),request.POST.get("option_2","off"),request.POST.get("option_3","off"),request.POST.get("option_4","off"))
		print("________",answered.index("on"))
		score = Score()
		score.user = request.user
		score.question = Question.objects.get(id = q_id)
		score.answered = 
		score.is_correct = 
		score.score = 

		score.save()
		return redirect('home')
	else:
		question = Question.objects.get(id = q_id)
		return render(request,"quiz/answer.html", {'question' : question})

