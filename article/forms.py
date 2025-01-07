from django import forms   
from .models import Article # Article modelini import ettik


class ArticleForm(forms.ModelForm): # hoca burada form.Form yerine ModelForm kullanmamız gerektiğini söyledi bağlantı kurabiliyormuşuz
    class Meta:
        model = Article
        fields = ['title','content','article_image'] # Article modelindeki title,content alanlarını formda göstermek için fields listesine ekledik