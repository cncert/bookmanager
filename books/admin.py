from django.contrib import admin
from .models import Book, User
# Register your models here.

admin.site.site_header = '图书管理系统'
admin.site.site_title = '图书管理系统'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', )
    fields = ('username', 'email')


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'reader', 'borrow_date', 'return_date', 'reminder', 'desc', )


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)