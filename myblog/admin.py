from django.contrib import admin
from .models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "timestamp")
    list_display = ("title", "timestamp", "author")
    prepopulated_fields = {"slug": ("title",)}

    


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post")


class QuotesAdmin(admin.ModelAdmin):
    list_display = ("quotes", "quote_by")


admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Signup)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Quotes, QuotesAdmin)
