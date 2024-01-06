from django.contrib import admin
from .models import Post, Country, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('destination_name', 'country_of_destination', 'author', 'status', 'created_on')
    search_fields = ['destination_name', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('destination_name',)}
    summernote_fields = ('content',)

admin.site.register(Country)
admin.site.register(Comment)