from django import forms
from .models import Post, Category, Comment
from django.contrib.auth import get_user
import time


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title for your blog here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title tag here'}),
            # 'category': forms.Select(attrs={'class': 'form-control'}),
            # 'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content of your blog here'}),
        }
    def __init__(self, *args, **kwargs):
            user = kwargs.pop('user', None)  # Get the current user from the keyword arguments
            super(PostForm, self).__init__(*args, **kwargs)

            # Automatically set the author field to the current user
            if user:
                self.fields['author'].initial = user
                self.fields['author'].widget = forms.HiddenInput()

class EditForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title for your blog here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title tag here'}),
            # 'category': forms.Select(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            # 'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content of your blog here'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name here', 'readonly': 'readonly'}),
            'name': forms.HiddenInput(),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment here'}),
        }

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')  # Remove 'request' from kwargs
        super(CommentForm, self).__init__(*args, **kwargs)
        user = get_user(request)

        if not user.is_authenticated:
            # If user is not logged in, set a default "Anonymous" name with a unique number
            timestamp = int(time.time())
            unique_number = f'Anonymous_{timestamp}'
            # unique_number = Comment.objects.count() + 1  # Adjust this logic as needed
            self.fields['name'].initial = unique_number
        else:
            # If user is logged in, set the name to the user's username or display name
            self.fields['name'].initial = user.username  # You can use user's display name if available

    def save(self, commit=True):
        # Your save logic here
        comment = super(CommentForm, self).save(commit=False)

        # If you need to set the name field explicitly before saving
        # comment.name = self.cleaned_data['name']

        if commit:
            comment.save()
        return comment
