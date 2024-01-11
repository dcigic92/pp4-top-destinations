from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = ''

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('destination_name', 'country_of_destination', 'featured_image', 'content',)

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('featured_image', 'content',)