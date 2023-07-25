from .models import Category


def menu_url(request):
    links = Category.objects.all()
    return dict(links=links)
