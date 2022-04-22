from django.shortcuts import render

from .models import Quesions

# Create your views here.
def index(request):
    return render(request , 'index.html')

def play(request):
    questions=Quesions.objects.all()
    if request.method == 'POST':
        questions=Quesions.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'questions': questions,
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            
        }
        return render(request,'result.html', context)
    else:
        questions=Quesions.objects.all()
    return render(request , 'play.html' ,{'questions':questions})

def result(request):
    return render(request , 'result.html')