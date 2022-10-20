from django.contrib import admin
from . models import Book, Farm, Post, Comment

# Register your models here.
admin.site.register(Farm)
admin.site.register(Book)
admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'post', 'created', 'active')
    list_filter=('active', 'created', 'updated')
    search_fields=('name', 'email', 'body')

