from .models import Question, Answer, Tag
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('question_title', 'question_text','creation_date', 'tags','score')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer_text', 'answer_score')

class TagSerializer(serializers.ListSerializer):
    class Meta:
        model= Tag
        field =('tag_name','tag_count')