from django.shortcuts import render
from django.http import HttpResponse


def index(request):
        
    return HttpResponse("欢迎访问图书管理系统！")