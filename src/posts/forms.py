from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Digite aqui o seu comentario!',
            'id': 'usercomment',
            'name': 'usercomment',
            'cols': '100',
            'rows': '10',
        })
    )

    class Meta:
        model = Comment
        fields = ('content',)
