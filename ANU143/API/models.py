from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=216, unique=True)
    year = models.IntegerField()
    language = models.CharField(max_length=216)
    img = models.URLField()

    def __str__(self):
        return self.title

class Season(models.Model):
    title = models.CharField(max_length=216, unique=True)
    season = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=216, unique=True)
    episode = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    download_link = models.URLField()

    def __str__(self):
        return self.title