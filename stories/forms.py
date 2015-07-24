from django.forms import ModelForm
from .models import Story
from django.contrib.auth.models import User
from django import forms

class StoryForm(ModelForm):

  class Meta:
    model = Story

    exclude = ('created_at', 'updated_at', 'points', 'moderator', 'voters')

class UserForm(ModelForm):

  class Meta:
    model = User
    fields = ('username', 'password',)
    widgets = {
      'password': forms.PasswordInput(),
    }

# class UserForm(ModelForm):

#   class Meta:
#     model = UserProfile
#     fields = ('')
