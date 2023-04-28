from django import forms
from .models import Review, Comment
from movies.models import Movie


class ReviewForm(forms.ModelForm):
    t = map(lambda x: tuple((x.pk, x.title)), Movie.objects.all())
    movie_title = forms.ChoiceField(choices=t)
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['review', 'user']
