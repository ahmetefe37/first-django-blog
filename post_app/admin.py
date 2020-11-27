from django.contrib import admin
from .models import Post


class AdminPostModel(admin.ModelAdmin):
    list_display = ["title", "pub_date", "slug"]
    list_display_links = ["pub_date"]
    list_editable = ["title"]
    list_filter = ["pub_date"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post


admin.site.register(Post, AdminPostModel)
