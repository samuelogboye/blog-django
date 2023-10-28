from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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


class EditForm(UserChangeForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
	is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
	is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
	date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')



class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

	class Meta:
		model = User
		fields = ('old_password', 'new_password','new_password2')

	def __init__(self, *args, **kwargs):
		super(PasswordChangingForm, self).__init__(*args, **kwargs)

		self.fields['old_password'].widget.attrs['placeholder'] = 'Enter your old password here'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter your new password here'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Enter your new password again here'