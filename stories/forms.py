from django.forms import ModelForm
from .models import Story
from django.contrib.auth.models import User

class StoryForm(ModelForm):

  class Meta:
    model = Story

    exclude = ('created_at', 'updated_at', 'points', 'moderator', 'voters')

class UserForm(ModelForm):

  class Meta:
    model = User
    fields = ('username', 'email', 'password',)

# class UserForm(ModelForm):

#   class Meta:
#     model = UserProfile
#     fields = ('')
