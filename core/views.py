from django.shortcuts import render
from .bs import get_watch
# Create your views here.

def index(request):
     context={}
     if request.method == 'POST':
          
             search_word = str(request.POST.get('search'))
             url = get_watch(search_word)
             context = {'url':url}
             return render(request , 'core/player.html', context)
           
          
     return render(request , 'core/search.html',context)