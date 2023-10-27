from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')

		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control'}),
			# 'first_name': forms.TextInput(attrs={'class':'form-control'}),
			# 'last_name': forms.TextInput(attrs={'class':'form-control'}),
			# 'email': forms.EmailInput(attrs={'class':'form-control'}),
			# 'password1': forms.PasswordInput(attrs={'class':'form-control'}),
			# 'password2': forms.PasswordInput(attrs={'class':'form-control'}),
		}

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['placeholder'] = 'Enter a unique Username'
		self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
		self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
		self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

