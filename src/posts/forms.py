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


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Conteúdo"
        self.fields['categories'].label = "Categorias"
        self.fields['previous_post'].label = "Próxima postagem"
        self.fields['next_post'].label = "Postagem anterior"

    title = forms.CharField(label="Título", widget=forms.TextInput(
        attrs={'class': 'input',
               'placeholder': 'Digite o título aqui'
               })
        )
    overview = forms.CharField(label="Descrição", widget=forms.Textarea(
        attrs={
            'class': 'overview-text-area',
            'placeholder': 'Digite aqui uma breve descrição',
            'cols': '100',
        })
    )
    thumbnail = forms.ImageField(label="Imagem")

    class Meta:
        model = Post
        fields = ['title',
                  'overview',
                  'content',
                  'thumbnail',
                  'categories',
                  'previous_post',
                  'next_post']
