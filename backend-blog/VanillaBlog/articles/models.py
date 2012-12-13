from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=254)
    content = models.TextField()
    
