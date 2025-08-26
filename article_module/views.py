from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DeleteView
from . import models
import markdown2



class articleListView(ListView):
    model = models.Article
    context_object_name = 'articles'
    template_name = 'article_module/article.html'


# def article_list(request):
#     articles=models.Article.objects.all()
#     return render(request,'article_module/article.html',{'articles':articles})

def article_detail(request,slug):
    article=get_object_or_404(models.Article,slug=slug)
    # article.content=markdown2.markdown(article.content)
    return render(request,'article_module/article_detail.html',{'article':article})