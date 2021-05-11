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
        article_post_form = ArticlePostForm(data=request.POST)
        # see if data submitted meets requirement of model
        if article_post_form.is_valid():
            # save data, but not to db for now
            new_article = article_post_form.save(commit=False)
            # specify user id in db as author
            new_article.author=User.objects.get(id=1)
            new_article.save()
            return redirect("article:article_list")
            # if data suer enter is invalid
        else:
            return HttpResponse("The content of the form is wrong, please fill in again.")
        # if the user request data
    else:
        article_post_form = ArticlePostForm()
        context= {
            'article_post_form' : article_post_form,
        }
        return render(request, 'article/create.html', context)

def article_list(request):
    # combine all blog post
    articles = ArticlePost.objects.all()
    # objects that ned to be passes to templates
    context = {
        'articles': articles
    }
    return render(request, 'article/list.html', context)

def article_details(request,id):
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

def article_delete(request, id):
    # capture article id to be deleted
    article = ArticlePost.objects.get(id = id)
    article.delete()
    return redirect("article:article_list")

def article_safe_delete(request, id):
    if request.method =='POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect('article:article_list')
    else:
        return HttpResponse("Only allow POSt requests!")