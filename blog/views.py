from django.shortcuts import render
from django.utils import timezone
from urllib.request import urlopen
from django.http import HttpResponse
import bs4
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def ktshop_source(request):
    ktshop_url = 'https://shop.kt.com/smart/agncyInfoView.do?vndrNo=AA01344'
    html = urlopen(ktshop_url)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    target_source = bsObj.find("ul", {"class":"ProdLst"})
    return HttpResponse(target_source)

