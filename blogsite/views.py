# -*- coding: utf-8 -*-
from unicodedata import category
from django.http.response import HttpResponse
from django.shortcuts import render
from blogsite.models import Blog, Category
from django.template import RequestContext


def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, 'blogsite/index.html', context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, 'blogsite/blogs.html', context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogsite/blog-details.html', {"blog": blog})

def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, 'blogsite/blogs.html', context)

def donates(request):
    return render(request, 'blogsite/donates.html')