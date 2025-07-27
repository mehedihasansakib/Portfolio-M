from django.contrib import admin
from .models import Category, Tag, Post
from markdownx.admin import MarkdownxModelAdmin

class CustomPostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('is_published', 'categories')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, CustomPostAdmin)
