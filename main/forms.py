from django import forms


class PostForm(forms.Form):
    author = forms.CharField(max_length=50, label='Автор')
    title = forms.CharField(max_length=200, label='Заголовок')
    text = forms.CharField(widget=forms.Textarea, label="Post Text")
    image = forms.ImageField(required=False)
