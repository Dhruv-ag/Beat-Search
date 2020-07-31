from django.shortcuts import render

from .models import Post
from django.db.models import Q
def drop(request):
    result=Post.objects.all()
    return render(request,'home.html',{'result':result})

# Create your views here.
