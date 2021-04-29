from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
from .forms import ArticlePostForm
from django.contrib.auth.models import User
import markdown

def article_create(request):
    # if user submits data
    if request.method == "POST":
        # assign submitted data to the form instance      
        article_post_from = ArticlePostForm(data=request.POST)
        # see if data submitted meets requirement of model
        if article_post_from.is_valid():
            # save data, but not to db for now
            new_article = article_post_from.save(commit=False)
            # specify user id in db as author
            

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
