from django.contrib import admin
from .models import Country, State, Tribe, BlogPost, Comment


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)
    search_fields = ('name',)


@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    list_filter = ('state',)
    search_fields = ('name',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'country', 'state', 'tribe', 'created_at')
    list_filter = ('country', 'state', 'tribe')
    search_fields = ('title', 'author')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'author_name', 'created_at')
    search_fields = ('author_name', 'text')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
