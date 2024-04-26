from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
       
        
class PostForm(forms.ModelForm):
    """ Create Post Form """
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 3})

    class Meta:
        """
        Get Post model, choose fields to display and add summernote widget
        """
        model = Post
        fields = [
        ]
        widgets = {
            'method': SummernoteWidget(),
        }

