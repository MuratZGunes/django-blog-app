from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin") # blank ve null true olduğu için doldurulması zorunlu değil
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date'] # created_date alanına göre sıralama yapar başına - koyduğumuz için en son ilk gösterilir

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments", verbose_name="Makale")
    comment_author = models.CharField(max_length=50, verbose_name="Yazar")
    comment_content = models.TextField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date'] # comment_date alanına göre sıralama yapar başına - koyduğumuz için en son ilk gösterilir