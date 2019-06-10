from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    """
    Allows users to submit blog posts
    """
    class Meta:
        model = Post
        """
        User editable fields
        """
        fields = ("title", "content", "published_date", "image", "tag")
        