from django.contrib import admin
from .models import category,blog
# Register your models here.
class blogAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':('title',)
    }
    list_display=('title','category','author','is_featured','status')
    search_fields=('id','title','category__category_name','status')
    list_editable=('is_featured',)
admin.site.register(category)
admin.site.register(blog,blogAdmin)