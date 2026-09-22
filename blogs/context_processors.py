from .models import category
from About.models import sociallinks

def get_catogories(request):
    categories=category.objects.all()
    return dict(categories=categories)
def get_sociallinks(request):
    social_links=sociallinks.objects.all()
    return dict(social_links=social_links)
