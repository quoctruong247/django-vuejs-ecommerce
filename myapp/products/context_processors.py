from .models import Category


def menu_categories(request):
    categories = Category.objects.filter(parent_id=None).filter(available=True)

    return {'menu_categories': categories}