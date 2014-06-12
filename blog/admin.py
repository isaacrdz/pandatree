from django.contrib import admin
from .models import Post
from sorl.thumbnail import get_thumbnail

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','imagen_album')

    def imagen_album(self, obj):
        return '<img src="%s">' % get_thumbnail(obj.image, '100x200', format='PNG').url # , crop='center'
    imagen_album.allow_tags = True



  

admin.site.register(Post, PostAdmin)