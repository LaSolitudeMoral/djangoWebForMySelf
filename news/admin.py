from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    # поля для вывода в окне редактора новости(например для отображения фотографии)
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return 'No photo'

    get_photo.short_description = 'Photo image'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' )
    list_display_links = ('id', 'title')
    search_fields = ('title',)  # Это кортеж поэтому нужна запятая


admin.site.register(News, NewsAdmin)
admin.site.register(Category)

admin.site.site_title = 'Управление новостями'
