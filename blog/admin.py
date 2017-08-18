# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'category',
                    'content', 'status', 'owner', 'created_time']
    list_filter = ('category', 'tags', 'status', 'created_time')
    search_fields = ('title', 'desc', 'owner')
    fieldsets = (
        (None,{
           'fields':(
               'title',
               'desc',
               ('category', 'tags'),
               'content',
               ('status', 'owner'),
           )
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'is_nav', 'owner', 'created_time')
    list_filter = ('status', 'is_nav', 'created_time')
    search_fields = ('name', 'owner')
    fieldsets = (
        (None,{
           'fields':(
               'name',
               ('status', 'is_nav'),
               'owner',
           )
        }),
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'owner', 'created_time')
    list_filter = ('status', 'created_time')
    search_fields = ('name', 'owner')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'status',
                'owner',
            )
        }),
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
