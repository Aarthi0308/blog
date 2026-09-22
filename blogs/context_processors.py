from .models import category

def get_catogories(request):
    categories=category.objects.all()
    return dict(categories=categories)
