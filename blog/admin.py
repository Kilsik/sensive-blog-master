from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'author', 'image', 'preview', 'text', 'tags',
        'published_at', 'likes']
    search_fields = ['title', 'slug', 'published_at', 'id',]
    list_display = ['title', 'id', 'author','published_at',]
    raw_id_fields = ['tags', 'likes',]
    list_filter = ['published_at', 'tags',]
    readonly_fields = ['preview',]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'post',]
    readonly_fields = ['published_at',]
    list_display = ['id', 'author', 'published_at', 'post',]
    search_fields = ['post', 'author','published_at', 'id',]
    list_filter = ['published_at',]
    list_select_related = ['post']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'id',]
