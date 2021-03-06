from django.conf.urls import url, include
from rest_framework import routers
from .views import index, add, submit, QuestionIndexView, question_detail, add_answer, QuestionViewSet, AnswerViewSet, increase_score, decrease_score
from .views import tagview



from .tagview import TagView, index


router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)

app_name = 'questions'
urlpatterns = [
    url(r'^_api$', include(router.urls)),
    url(r'^$', QuestionIndexView.as_view(), name='index'),
    
    url(r'^add$', add, name='add'),  # Urls with trailing slash do not work, Think how to make it optional

    url(r'^add/submit$', submit, name='submit'),

    url(r'^questions/(?P<question_id>[0-9]+)$', question_detail, name='detail'),

    url(r'^(?P<question_id>[0-9]+)/answer$', add_answer, name='answer'),
    url(r'^add_score/(?P<question_id>[0-9]+)$',increase_score, name='increase_score'),
    url(r'^/sub_score/(?P<question_id>[0-9]+)$',decrease_score, name='decrease_score'),
    url(r'^tags$', index, name='tagIndex'),
    url(r'^tags/_api$', TagView.as_view(), name='tagIndex')

]