from django import forms
from .models import Books, Comments

class PostForm(forms.ModelForm ):
    class Meta:
        model = Books
        fields = ['title', 'released_year', 'description', 'author']

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Comments
        fields = ['body']