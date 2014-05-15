from blog.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views')

admin.site.register(Post, PostAdmin)