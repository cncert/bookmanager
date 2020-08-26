from django.contrib import admin
from .models import Book, User
from books.forms import UserAdminForm
# Register your models here.

admin.site.site_header = '图书管理系统'
admin.site.site_title = '图书管理系统'


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ('username', 'email', 'books_of_user')
    fields = ('username', 'email')

    def  books_of_user(self, obj):
        if not obj.reader.all():
            return ""
        return "、".join(['《' + book.name + '》' for book in obj.reader.all()])
    books_of_user.short_description = "借阅书籍"


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'reader', 'borrow_date', 'return_date', 'reminder', 'desc', )


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)