import datetime
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.utils.timezone import utc
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Story
from .forms import StoryForm, UserForm

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
  if request.user.is_authenticated():
    liked_stories = request.user.liked_stories.filter(id__in=[story.id for story in stories])
  else:
    liked_stories = []
  context = {
    'stories': stories,
    'user': request.user,
    'liked_stories': liked_stories,
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

@login_required
def vote(request):
  story = get_object_or_404(Story, pk=request.POST.get('story'))
  story.points += 1
  story.save()
  user = request.user
  user.liked_stories.add(story)
  user.save()
  return HttpResponse()

def register_page(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(user.password)
      user.save()
      return redirect('/login/')
  else:
    form = UserForm()    
  return render(request, 'stories/login_page.html', {
    'form': form
  })
