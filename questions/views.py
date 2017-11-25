from django.shortcuts import render, reverse, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed
from django.views import generic
import datetime
from .models import Question, Answer, Tag
import markdown
import logging
from rest_framework import viewsets
from .serializers import QuestionSerializer, AnswerSerializer
# Create your views here.

logger = logging.getLogger(__name__)

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
    ans = Answer.objects.filter(question_id=question_id).order_by('-answer_date')[:10]
    context= {
        'question':q,
        'answer':ans
    }
    return render(request, 'questions/question_detail.html', context)

def add_answer(request, question_id):
    if request.method =='GET':
        return redirect('questions:detail')
    else:
        answer = Answer();
        answer.answer_text = request.POST['answer_text']
        answer.answer_date = datetime.datetime.now()
        answer.answer_score=0
        answer.question_id = question_id;
        answer.save(force_insert=True);
        return HttpResponseRedirect(reverse('questions:index'))

def increase_score(request, question_id):
    if request.method !='POST':
        return HttpResponseNotAllowed("")
    else:
        q=Questions.objects.get(id=question_id)
        q.score= q.score+1;
        q.save();
        return JsonResponse({'newscore':q.score});
             

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()#.order_by('-date_joined')
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer