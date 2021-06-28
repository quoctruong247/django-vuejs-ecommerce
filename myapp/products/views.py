from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q
from cart.cart import Cart
import random
from datetime import datetime
from carousel.models import Carousel
from django.http import JsonResponse
from django.utils.text import Truncator
import json
# Create your views here.
def category_detail(request, slug):
    
    # Category query
    categories = Category.objects.filter(available=True)
    # Carousel query for slide Category Detail
    category_carousels = Carousel.objects.filter(available=True).filter(parent_id=2)
    #Query a category
    category = get_object_or_404(Category, slug=slug)
    #Query all Product
    products = category.products.filter(parent=None).order_by('title')
    productsstring_category =''
    
    for item in products:
        itemTitle = item.title.replace('"',r'\"')
        title=Truncator(itemTitle).words(10, truncate='...')

        if item.priceRange != None:
            maxi=max(item.priceRange.values())
            mini=min(item.priceRange.values())
        else:
            maxi = '' 
            mini = ''
        
        url = '/%s/%s/' % (item.category.slug, item.slug)    
        b = '{"id": "%s", "title": "%s", "price": "%s", "sale_price": "%s", "maxi": "%s", "mini": "%s", "thumbnail": "%s","url": "%s"},' % (item.id, title, item.price,item.sale_price, maxi, mini, item.thumbnail.url, url)
        productsstring_category = productsstring_category + b

    context = {
        'title': 'Category-detail page',
        'categories': categories,
        'category': category,
        'products': products,
        'category_carousels': category_carousels,
        'productsstring_category': productsstring_category.rstrip(','),
    }

    return render(request, 'category_detail.html', context)


def product_detail(request, category_slug, slug):
    product_carousels = Carousel.objects.filter(available=True).filter(parent_id=3)
    product = get_object_or_404(Product, slug=slug)
    product.num_visits = product.num_visits + 1
    product.last_visit = datetime.now()
    product.save()

    # Add review
    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')
        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)

        return redirect('product_detail', category_slug=category_slug, slug=slug)

    # related_product
    related_products = list(product.category.products.filter(parent=None).exclude(id=product.id))

    if len(related_products) >= 3:
        related_products = random.sample(related_products, 3)

    if product.parent:
        return redirect('product_detail', category_slug=category_slug, slug=product.parent.slug)

    imagesstring = "{'thumbnail': '%s', 'image': '%s'}," % (product.thumbnail.url, product.image.url)

    for image in product.images.all():
        imagesstring = imagesstring + ("{'thumbnail': '%s', 'image': '%s'}," % (image.thumbnail.url, image.image.url))

    cart = Cart(request)

    if cart.has_product(product.id):
        product.in_cart = True
    else:
        product.in_cart = False

    # json product
    title = product.title.replace('"',r'\"')
    description = product.description.replace('"',r'\"')
    #url = '/%s/%s/' % (product.category.slug, product.slug)    
    #productstring = '{"id": "%s", "title": "%s","description": "%s", "price": "%s","priceRange": "%s", "thumbnail": "%s","url": "%s"},' % (product.id, title,description, product.price ,product.priceRange, product.thumbnail.url, url)
    #priceRangeString = json.dumps(product.priceRange,indent = 4)
    name_price=''
    for k,v in product.priceRange.items():
        s='{"id":"%s","title":"%s","description":"%s","name":"%s","price":"%s","qty":"%s",},' %(product.id,title,description, k, v, 1)
        name_price = name_price + s

    #priceRangeString = product.priceRange
    print(name_price)
    context = {
        'title': 'Product detail page',
        'product': product,
        'imagesstring': imagesstring,
        'related_products': related_products,
        'product_carousels': product_carousels,
        #'productstring': productstring,
        #'priceRangeString': priceRangeString,
        'name_price':name_price,
    }

    return render(request, 'product_detail.html', context)


def search(request):
    query = request.GET.get('query')
    instock = request.GET.get('instock')
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 100000)
    sorting = request.GET.get('sorting', '-created_at')
    categories_search = Category.objects.filter(Q(name__icontains=query)).filter(available=True)
    products = Product.objects.filter(Q(title__icontains=query)).filter(available=True)
    # products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(price__gte=price_from).filter(price__lte=price_to)

    if instock:
        products = products.filter(num_available__gte=1)

    context = {
        'title': 'Search page',
        'query': query,
        'instock': instock,
        'price_from': price_from,
        'price_to': price_to,
        'products': products.order_by(sorting),
        'sorting': sorting,
        'categories_search':categories_search
    }

    return render(request, 'search.html', context)