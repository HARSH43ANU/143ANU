from django.urls import path, include
from .views import contents, home, index, random_content, random_content_viewer

urlpatterns = [
    path('index', view=index, name='index-page'),
    path('home', view=home, name='home-page'),
    path('contents', view=contents, name='content-page'),
    path('random_content_viewer', view=random_content_viewer, name='random-content-viwer'),
    ## APIs
    path('api/random_content', view=random_content, name='random-content-api'),
]