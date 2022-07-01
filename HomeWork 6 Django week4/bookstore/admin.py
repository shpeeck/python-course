from django.contrib import admin
from .models import Autors, Books, Comments


admin.site.register(Autors)
# admin.site.register(Comments)

class BooksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Books._meta.fields]
    search_fields = ['id', 'title', 'released_year', 'author_id']
    list_filter = ['author_id']
    list_editable = ('title', 'released_year')

    class Meta:
        model = Books

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created',)
    list_filter = ('created', 'updated')
    search_fields = ('name', 'body')

admin.site.register(Books, BooksAdmin)
admin.site.register(Comments, CommentAdmin)

