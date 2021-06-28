from django.shortcuts import render, get_object_or_404
from products.models import Product, Category
from carousel.models import Carousel
# from order.models import Order


# def order_confirmation(request):
#     order = Order.objects.get(pk=45)
#
#     return render(request, 'order_confirmation.html', {'order': order})


def index(request):
    products = Product.objects.filter(available=True).order_by('title')
    categories = Category.objects.filter(available=True)
    carousels = Carousel.objects.filter(available=True).filter(parent_id=1)
    featured_products = Product.objects.filter(feature=True).filter(available=True)
    featured_categories = Category.objects.filter(feature=True).filter(parent_id=None).filter(available=True)
    popular_products = Product.objects.all().order_by('-num_visits')[0:4]
    recently_viewed_products = Product.objects.all().order_by('-last_visit')[0:4]

    context = {
        'categories': categories,
        'products': products,
        'carousels': carousels,
        'popular_products': popular_products,
        'recently_viewed_products': recently_viewed_products,
        'featured_products': featured_products,
        'featured_categories': featured_categories,
        'title': 'TSDI eCommerce'
    }

    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'about page'
    }

    return render(request, 'about.html', context)


def contact(request):
    context = {
        'title': 'contact page'
    }

    return render(request, 'contact.html', context)


def reorder(request):
    context = {
        'title': 'reorder page'
    }

    return render(request, 'reorder.html', context)
