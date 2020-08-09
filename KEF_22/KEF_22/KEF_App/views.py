from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from .models import Teacher_Query
from .models import Assesment


def home(request):
    return render(request, 'home.html')

@login_required
def quiz_page(request):
  assesments = Assesment.objects.all()[:10]

  context = {
    'title': 'Latest Quizes',
    'assesments': assesments
  }

  return render(request, 'quiz_page.html', context)

@login_required
def queries_teacher(request):
  queries = Teacher_Query.objects.all()[:10]

  context = {
    'title': 'Latest Posts',
    'queries': queries
  }

  return render(request, 'queries_teacher.html', context)
