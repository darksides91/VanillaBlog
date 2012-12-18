from django.views.generic import ListView
from vanilla.articles.models import Article

class ArticlesView(ListView):

    template_name = "articles/articles-list.html"
    model = Article
