from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
from .forms import ArticlePostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import markdown
# paging module
from django.core.paginator import Paginator



# CREATE
@login_required(login_url='/userprofile/login/')
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
            new_article.author= User.objects.get(id= request.user.id)
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

# Show All article_safe_delete
def article_list(request):
    # combine all blog post
    articles_list = ArticlePost.objects.all()
    # display 1 article per page
    paginator = Paginator(article_list, 1)
    # get page number in url
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    # objects that ned to be passes to templates
    context = {
        'articles': articles
    }
    return render(request, 'article/list.html', context)

# READ
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

# UPDATE
def article_update(request, id):
    # retrieve specific article object that is going to be modified
    article = ArticlePost.objects.get(id=id)
    # determine whether user submits the form data as POST
    if request.method == 'POST':
        # assign data to the form instance
        article_post_form = ArticlePostForm(data = request.POST)
        # does data submitted meet the requirements for model
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect('article:article_detail', id=id )
        else: 
            return HttpResponse('The content of the form is incorrect, please fill again.')
    # if User sends GET request
    else:
        # create a form class instance
        article_post_form = ArticlePostForm()
        # assign a context, pass the article object in to extract old content
        context = {
            'article': article,
            'article_post_form' : article_post_form
        }
        return render(request, 'article/update.html', context)

def article_delete(request, id):
    # capture article id to be deleted
    article = ArticlePost.objects.get(id = id)
    article.delete()
    return redirect("article:article_list")

# DELETE
# Safely Delete the article, passing ID to function
def article_safe_delete(request, id):
    if request.method =='POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect('article:article_list')
    else:
        return HttpResponse("Only allow POSt requests!")

