from django.contrib import admin
from .models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'tags_text')

    def created_at(self, obj):
        return obj.createdAt

admin.site.register(Category)
admin.site.register(Tag)