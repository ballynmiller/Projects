from django import forms 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from websites.contact.models import Subscriber,Contact

class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    image=forms.ImageField()
    description=forms.CharField()

class UserForm(UserCreationForm):
    firstname=forms.CharField(label='First Name', max_length=30)
    lastname=forms.CharField(label='Last Name', max_length=30)
    email=forms.EmailField()
    
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name=self.cleaned_data['firstname']
        user.last_name=self.cleaned_data['lastname']
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class UserContactForm(ModelForm):
    class Meta: 
        model=Contact
        exclude=('user',)
    
class SubscribeForm(ModelForm):
    class Meta:
        model=Subscriber
        fields=["email"]
