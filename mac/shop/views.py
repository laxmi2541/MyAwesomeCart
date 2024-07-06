import django.shortcuts


def index(request):
    return django.shortcuts.render(request, 'shop/index.html')
def about(request):
    return django.shortcuts.render(request, 'shop/about.html')


def checkout():
    return None