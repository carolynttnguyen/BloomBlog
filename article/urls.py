from django.urls import path
# import views.py
from . import views

app_name = 'article'

urlpatterns = [
    # article list
    path('article-list', views.article_list, name ='article_list'),
    # READ article details
    path('article-detail/<int:id>/', views.article_details, name='article_detail'),
    # CREATE article
    path('article-create/', views.article_create, name='article_create'),
    # UPDATE article
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    # DELETE article
    # path('article-safe-delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
]