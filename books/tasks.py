import time

from django.conf import settings
from django.core.mail import send_mail

from books.models import Book

subject = settings.SUBJECT
message = "您好， \n    您借阅的图书《%s》到期了，请与图书管理员联系换书。"
auth_user = settings.EMAIL_HOST_USER
auth_password = settings.EMAIL_HOST_PASSWORD
from_email = auth_user

def scan_user():
    books = Book.objects.all()
    for book in books:
        return_date = book.return_date
        if return_date:
            return_date = return_date.strftime("YYYY-MM-DD")
            reader_email = book.reader.email
            today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            if return_date  == today:
                send_mail(subject=subject, message=message, from_email=from_email, auth_user=auth_user, auth_password=auth_password, recipient_list=[reader_email])
