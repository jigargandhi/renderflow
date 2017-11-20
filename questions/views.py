from django.shortcuts import render, reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import generic
import datetime
from .models import Question, Answer, Tag
import markdown
# Create your views here.


def index(request):
    return render(request, 'questions\index.html')


class QuestionIndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.all()#.order_by('-creation_date')[:5]

def add(request):
    return render(request,'questions/add.html')


def submit(request):
    if request.method == 'GET':
        return HttpResponseRedirect('questions:index')
    else:
        question = Question()
        question.question_text = request.POST['question_text']
        question.question_title = request.POST['question_title']
        question.score = 0
        question.save()
        return HttpResponseRedirect(reverse('questions:index'))


def question_detail(request, question_id):
    q = Question.objects.get(id=question_id)
    q.question_text = markdown.markdown(q.question_text)
    context= {
        'question':q
    }
    return render(request, 'questions/question_detail.html', context)