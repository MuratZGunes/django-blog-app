from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm # ArticleForm'u import ettik
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"index.html") 

def about(request):
    return render(request,"about.html") 

@login_required(login_url = "user:login") # login olmadan dashboard'a erişemezsin
def dashboard(request):
    articles = Article.objects.filter(author = request.user) # Article modelindeki author alanı request.user olanları getir
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context) 

@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None) # ArticleForm'u form değişkenine atadık
    if form.is_valid(): # form doğruysa
        article = form.save(commit=False)   # sen save işlemini gerçekleştirme ben kendim gerçekleştirecem bunu id ve authoru belirtmediğimiz için commit=False dedik
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("article:dashboard")

    return render(request,"addarticle.html",{"form":form}) # addarticle.html dosyasını döndürür ve formu gönderir

def detail(request,id):
    # article = Article.objects.filter(id = id).first() # Article modelindeki id'si id olanı getir
    article = get_object_or_404(Article,id = id) # Article modelindeki id'si id olanı getir eğer yoksa 404 döndür

    comments = article.comments.all() # article'ın comment'lerini getir

    return render(request,"detail.html",{"article":article,"comments":comments}) # detail.html dosyasını döndürür ve article'ı gönderir

@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id) # Article modelindeki id'si id olanı getir eğer yoksa 404 döndür
    form = ArticleForm(request.POST or None, request.FILES or None,instance = article) # ArticleForm'u form değişkenine atadık ve instance'ı article yaptık
    if form.is_valid(): # form doğruysa
        article = form.save(commit=False)   
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla güncellendi")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form}) # update.html dosyasını döndürür ve formu gönderir

@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id) # Article modelindeki id'si id olanı getir eğer yoksa 404 döndür
    article.delete() # article'ı sil
    messages.success(request,"Makale başarıyla silindi")
    return redirect("article:dashboard") # dashboard'a git

def articles(request):
    keyword = request.GET.get("keyword") # keyword değişkenine url'den gelen keyword'ü atadık
   
    if keyword: # eğer keyword varsa
        articles = Article.objects.filter(title__contains = keyword) # Article modelindeki title'ı keyword'ü içeren article'ları getir
        return render(request,"articles.html",{"articles":articles}) # articles.html dosyasını döndürür ve article'ları gönderir
    
    articles = Article.objects.all() # Article modelindeki tüm article'ları getir eğer keyword yoksa
    return render(request,"articles.html",{"articles":articles})

def searchArticle(request):
    if request.method == "GET":
        search_query = request.GET.get("search_query")
        
        if search_query:
            articles = Article.objects.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            ).order_by('-created_date')
            
            return render(request, "articles.html", {
                "articles": articles,
                "search_query": search_query
            })
    
    return redirect("article:articles")

def addComment(request,id):
    article = get_object_or_404(Article,id = id) # Article modelindeki id'si id olanı getir eğer yoksa 404 döndür
    
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author,comment_content = comment_content)
        newComment.article = article
        newComment.save()
         
    return redirect(reverse("article:detail",kwargs={"id":id})) # detail sayfasına git
    