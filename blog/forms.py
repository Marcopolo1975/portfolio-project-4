from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget




class CommentForm(forms.ModelForm):
    """ Create Comment Form """
    class Meta:
        model = Comment
        fields = ('body',)
        
       
        
class PostForm(forms.ModelForm):
    """ Create Post Form """
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        #self.fields[''].widget = forms.Textarea(attrs={'rows': 3})

    class Meta:
        """
        Get Post model, choose fields to display and add summernote widget
        """
        model = Post
        fields = ['title', 'image', 'excerpt', 'content' ]
        widgets = {
            'method': SummernoteWidget(),
        }
