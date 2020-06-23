from django import forms
from .models import Article, Comment


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )
        # 수정이 일어나지 않는다는 의미로 tuple을 사용한다.
        # () -> tuple (가변X)
        # [] -> list (가변형)
        # 완전히 동일한 구조. 둘 다 반복 가능함.

        '''
        exclude = ['article', ] -> 내가 제거할 것만 선택
        '''
        #exclude = 