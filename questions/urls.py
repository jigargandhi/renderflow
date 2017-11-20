from django.conf.urls import url

from .views import index, add, submit, QuestionIndexView, question_detail


app_name = 'questions'
urlpatterns = [

    url(r'^$', QuestionIndexView.as_view(), name='index'),

    url(r'^add$', add, name='add'),  # Urls with trailing slash do not work, Think how to make it optional

    url(r'^add/submit$', submit, name='submit'),

    url(r'^(?P<question_id>[0-9]+)', question_detail, name='detail')
]