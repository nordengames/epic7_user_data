from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Question

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.") #http://140.238.63.114:8000/polls/
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question': question})
