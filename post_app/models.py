from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Post(models.Model):
    user = models.ForeignKey("auth.User",verbose_name="Yazar", related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    pub_date = models.DateTimeField(verbose_name="Tarih", auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:details_url", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("post:update_url", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("post:delete_url", kwargs={"slug": self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-pub_date", "id"]

# Yorum Sınıfı tasarımı
class Comment(models.Model):
    post = models.ForeignKey("post_app.Post", related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="İsim")
    content = models.TextField(verbose_name="Yorum İçeriği")
    created_date = models.DateTimeField(auto_now_add=True)