from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='영화 제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title form-control',
                'placeholder' : '한글 제목을 입력하세요.',
            }
        )
    )
    
    title_en = forms.CharField(
        label='영화 제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title form-control',
                'placeholder' : '영문 제목을 입력하세요.',
            }
        )
    )
    
    audience = forms.IntegerField(
        label='관객 수',
        widget=forms.NumberInput(
            attrs={
                'class' : 'my-title form-control',
            }
        )
    )

    open_date = forms.DateField(
        label='개봉일',
        widget=forms.DateInput(
            attrs={
                'class' : 'my-title form-control',
            }
        )
    )

    genre = forms.CharField(
        label='장르',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title form-control',
                'placeholder' : 'Ex) 드라마/스릴러',
            }
        )
    )

    watch_grade = forms.CharField(
        label='관람 등급',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title form-control',
                'placeholder' : 'Ex) 15세 관람가',
            }
        )
    )

    score = forms.FloatField(
        label='평점',
        widget=forms.NumberInput(
            attrs={
                'class' : 'my-title form-control',
            }
        )
    )

    poster_url = forms.CharField(
        label='사진 경로',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title form-control',
                'placeholder' : 'Ex) https://movie-phinf.pstatic.net/20200610_45/1591752004615kLWYv_JPEG/movie_image.jpg',
            }
        )
    )

    description = forms.CharField(
        label='상세 설명',
        widget=forms.Textarea(
            attrs={
                'class':'my-content form-control',
                'placeholder' : '내용을 입력해주세요.',
                'col' : 50,
                'row' : 30,

            }
        )
    )
    

    class Meta:
        model = Movie
        fields = '__all__'