from django import forms
from .models import Post, Category
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
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
            # 'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content of your blog here'}),
            'body': TinyMCE(attrs={'cols': 80, 'rows': 30}), # TinyMCE widget
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
			 'body': TinyMCE(attrs={'cols': 80, 'rows': 30}), # TinyMCE widget
        }