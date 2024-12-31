from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms

class SignUp(UserCreationForm):
    email=forms.EmailField(label='',widget=forms.TextInput(attrs={'class':"form-control" , 'placeholder':"Email"}))
    first_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"First Name" }))
    last_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
    
    def __init__(self,*args,**kwargs):
        super(SignUp,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User_name'
        self.fields['username'].label=''
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Require 150 Characters or fewer</small>'
      
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']="Password"
        self.fields['password1'].label=''
        self.fields['password1'].help_text='<ul class="form-text text-muted small"><li> Your password can\'t be similar to your personal info</li></ul>'

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']="Confirm Password"
        self.fields['password2'].label=''
        self.fields['password2'].help_text='<ul class="form-text text-muted small"><li> Your password should be similar to your password</li></ul>'