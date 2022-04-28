from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Quesions

# Create your views here.
def index(request):
    return render(request , 'index.html')

@login_required
def play(request):
    questions=Quesions.objects.all()
    if request.method == 'POST':
        questions=Quesions.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions: 
            response = request.POST.get(str(q.id)) #to get the value of radio options we convert it into str
            total += 1 
            if q.ans ==  response:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) *100
        context = {
            'questions': questions,
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
        }
        return render(request,'result.html', context)
    else:
        questions=Quesions.objects.all()
    return render(request , 'play.html' ,{'questions':questions})
