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
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title for your blog here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title tag here'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            # 'category': forms.Select(attrs={'class': 'form-control'}),
            # 'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content of your blog here'}),
            'body': TinyMCE(attrs={'cols': 80, 'rows': 30}), # TinyMCE widget
        }


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