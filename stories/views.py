import datetime
from django.shortcuts import render, render_to_response, redirect
from django.utils.timezone import utc
from django.contrib.auth.decorators import login_required

from .models import Story
from .forms import StoryForm

def score(story, gravity=1.8, timebase=120):
  points = (story.points - 1)**0.8
  now = datetime.datetime.utcnow().replace(tzinfo=utc)
  age = int((now - story.created_at).total_seconds()) / 60
  return points / (age + timebase) ** 1.8

def top_stories(top=180, consider=1000):
  latest_stories = Story.objects.all().order_by('-created_at')[:consider]
  ranked_stories = sorted([(score(story), story) for story in latest_stories], reverse=True)
  return [story for _, story in ranked_stories][:top]

# Create your views here.
def index(request):
  stories = top_stories(top=30)
  context = {
    'stories': stories,
    'user': request.user,
  }
  return render(request, 'stories/index.html', context)

@login_required
def story(request):
  if request.method == 'POST':
    form = StoryForm(request.POST)
    if form.is_valid():
      story = form.save(commit=False)
      story.moderator = request.user
      story.save()
      return redirect('/')
  else:
    form = StoryForm()
  return render(request, 'stories/story.html', {
    'form': form
  })
