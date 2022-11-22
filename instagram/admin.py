from django.contrib import admin
from .models import Post

# Register your models here.

# Python 장식자 @ 문법은 어떠한 대상이라도 감싸는 것 (Wrapping) 감싼 대상의 기능을 커스텀 가능
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']

    def message_length(self, Post):
        return "{}".format()