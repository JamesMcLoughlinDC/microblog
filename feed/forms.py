from django import forms
from .models import Comments, Post

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		widgets = {
          'blog_text': forms.Textarea(attrs={'rows':10, 'cols':40}),
        }
		fields = ['description','blog_text','pic', 'tags']

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']



        