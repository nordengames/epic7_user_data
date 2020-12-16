from django.shortcuts import render

# Create your views here.
from .models import Character

def index(request):
  character_list = Character.objects.order_by('-pub_date')[:5]
  context = {"character_list": character_list}
  return render(request, 'user_data/index.html', context)