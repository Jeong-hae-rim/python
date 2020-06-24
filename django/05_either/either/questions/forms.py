from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('user',) 
        #('user') -> 쉼표를 안 쳐주면 튜플로 인식을 하지 않음 아무 의미 없음


class AnswerForm(forms.ModelForm):

    CHOICES = [
        ('a', 'RED'),
        ('b', 'BLUE'),
    ]

    choice = forms.ChoiceField(
        choices=CHOICES
    )

    class Meta:
        model = Answer
        exclude = ('user', 'question',)