from django.shortcuts import render
from django.utils import timezone
from urllib.request import urlopen
from bs4 import BeautifulSoup
from .models import Post, Product

ktshop_url = "https://m.shop.kt.com:444/m/smart/agncyInfoView.do?vndrNo=AA01344"

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def ktshop_product_info(request):

    item_name = {}
    item_price = {}
    item_code = {}
    thumbs_link = {}

    html = urlopen(ktshop_url)
    bsObj = BeautifulSoup(html, "html.parser")
    thumbs_blocks = bsObj.findAll("div", {"class": "thumbs"})
    prodInfo_blocks = bsObj.findAll("div", {"class": "prodInfo"})

    for idx, prodInfo in enumerate(prodInfo_blocks):
        item_name[idx] = prodInfo.ul.find("li", {"class": "prodName"}).text
        item_price[idx] = int(prodInfo.ul.find("li", {"class": "prodPrice"}).span.text.replace(',',''))
        href_value = prodInfo.ul.find("li", {"class": "prodSupport"}).findAll("a")[0].attrs['href']
        item_code[idx] = href_value[25:35]

    for idx, thumbs in enumerate(thumbs_blocks):
        thumbs_link[idx] = thumbs.findAll("img")[0].attrs['src']
        Product(name=item_name[idx], price=item_price[idx], code=item_code[idx], img_link=thumbs_link[idx]).save()

    products = Product.objects.filter()

    return render(request, 'blog/ktshop.html', {'products': products})
