from django.conf.urls import url, include
from rest_framework import routers
from .views import index, add, submit, QuestionIndexView, question_detail, add_answer, QuestionViewSet, AnswerViewSet, increase_score, decrease_score
from .views import tagview




router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)

app_name = 'questions'
urlpatterns = [
    url(r'^_api$', include(router.urls)),
    url(r'^$', QuestionIndexView.as_view(), name='index'),
    
    url(r'^add$', add, name='add'),  # Urls with trailing slash do not work, Think how to make it optional

    url(r'^add/submit$', submit, name='submit'),

    url(r'^(?P<question_id>[0-9]+)$', question_detail, name='detail'),

    url(r'^(?P<question_id>[0-9]+)/answer$', add_answer, name='answer'),
    url(r'^(?P<question_id>[0-9]+)/add_score$',increase_score, name='increase_score'),
    url(r'^(?P<question_id>[0-9]+)/sub_score$',decrease_score, name='decrease_score'),
    url(r'^tags/$', tagview, name='tagview')
]