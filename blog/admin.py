from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Contact, Category, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post', 'created_at')


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "preview", "image", "created_at", "is_published")
    search_fields = ("title", "description")

    def preview(self, obj):
        return format_html(f"<img width=50 height=50 src='{obj.image.url}'")


class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "is_solved")


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
