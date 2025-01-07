from django.contrib import admin
from django.urls import path

from article import views # article uygulamasındaki views.py dosyasını import et

app_name = 'article'

urlpatterns = [
    path("dashboard/",views.dashboard,name = 'dashboard'),
    path("addarticle/",views.addArticle,name = 'addarticle'),
    path("article/<int:id>/",views.detail,name = 'detail'),
    path("update/<int:id>/",views.updateArticle,name = 'updatearticle'),
    path("delete/<int:id>/",views.deleteArticle,name = 'delete'),
    path("",views.articles,name = 'articles'),
    path('search/', views.searchArticle, name='search'),
    path('comment/<int:id>/', views.addComment, name='comment'),
]
