from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from API.models import Content, Post

# Create your views here.
def index(request):
    return render(request, template_name='index.html')

# home page loader
def home(request):
    post = Post.objects.order_by('?')[0]
    return render(request, template_name='home.html', context={
        'post': post,
    })

# contents page loader
def contents(request):
    return render(request, template_name='contents.html')

def random_content_viewer(request):
    return render(request, template_name='random_content_viewer.html')

# APIs
# get random_content
def random_content(request):
    content = Content.objects.order_by('?')[0]
    return JsonResponse({
        'title': content.title,
        'episode': content.episode,
        'season': content.season.title,
        'download_link': content.download_link,
        'img': content.season.post.img,
    })