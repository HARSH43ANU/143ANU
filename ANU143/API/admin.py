from django.contrib import admin
from .models import Post, Content, Season
# Register your models here.

admin.site.register(Post)
admin.site.register(Season)
admin.site.register(Content)