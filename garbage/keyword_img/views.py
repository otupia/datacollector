from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def image_detail(request, image_code):
    return render(request, "detail.html", {"title":image_code})
