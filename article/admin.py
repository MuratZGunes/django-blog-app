from django.contrib import admin

# Register your models here.

from .models import Article, Comment

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date"] # admin panelinde hangi alanların gösterileceğini belirtir
    list_display_links = ["title", "created_date"]     # title ve created_date alanlarının link olmasını sağlar
    search_fields = ["title"]       # title alanında arama yapılmasını sağlar
    list_filter = ["created_date"]      # created_date alanına göre filtreleme yapılmasını sağlar
    class Meta  : # bu class django tarafından söylenen bir şey
        model = Article # bu classın hangi model ile ilişkili olduğunu belirtir