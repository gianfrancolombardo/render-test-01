"""Api admin."""

# Django
from django.contrib import admin

# Models
from render_test_01.api.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ('title','created')
    search_fields = ('title',)
    list_filter = ('created',)

 