from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import markdown


def article_list(request):
    # combine all blog post
    articles = ArticlePost.objects.all()
    # objects that ned to be passes to templates
    context = {
        'articles': articles
    }
    return render(request, 'article/list.html', context)


def article_details(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                     ])
    context = {
        'article': article,
    }
    return render(request, 'article/detail.html', context)
