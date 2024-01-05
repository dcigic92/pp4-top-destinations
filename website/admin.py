from django.contrib import admin
from .models import Post, Country
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

admin.site.register(Country)