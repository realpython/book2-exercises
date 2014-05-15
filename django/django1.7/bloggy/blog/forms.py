from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    created_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())
    tag = forms.CharField(required=False, max_length=20)
    image = forms.ImageField(required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Post
        fields = ['created_at', 'title', 'content', 'tag', 'image', 'views']