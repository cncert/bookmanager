from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from books.models import Book
import datetime
import time
from django.conf import settings
import smtplib
from email.mime.text import MIMEText

subject = settings.SUBJECT
message = "您好， \n    您借阅的图书《%s》到期了，请与图书管理员联系换书。"
auth_user = settings.EMAIL_HOST_USER
auth_password = settings.EMAIL_HOST_PASSWORD
from_email = auth_user



def send_email(from_email, receiver, auth_user, auth_password, subject, message):
    msg = MIMEText(message, 'html', 'utf-8')
    msg['From']="图书管理员"
    msg['To']=receiver
    msg['Subject']=subject

    sender = smtplib.SMTP_SSL('smtp.qq.com')# 获取江建有奖传输协议证书
    sender.connect('smtp.qq.com', '465')# 设置发送域名，端口465
    sender.login(auth_user, auth_password)
    sender.sendmail(from_email, receiver, msg.as_string())
    sender.close()
    print("发送完毕")


def index(request):
    books = Book.objects.all()
    for book in books:
        return_date = book.return_date
        book_name = book.name
        if return_date:
            return_date = return_date.strftime('%Y-%m-%d')
            reader_email = book.reader.email
            today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            if return_date  == today:
                send_email(from_email, reader_email, auth_user, auth_password, subject, message%book_name)
        
    return HttpResponse("欢迎访问图书管理系统！")