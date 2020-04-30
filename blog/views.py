from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Post

# posts = [
#     {
#         'author': 'Sneha Gupta',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 29, 2020'
#     },
#     {
#         'author': 'Sg',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 29, 2020'
#     }
# ]

def home(request):
    context = {
        "posts":Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model = Post
    

def about(request):
    return render(request,'blog/about.html',{'title':'ABOUT'})
