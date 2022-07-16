from dashboard.models import Blog, BlogCategories

def menus(context):
    return {'menus': BlogCategories.objects.filter(visible_menu=True)}

def latest(context):
    return {'new': Blog.objects.all()[:5]}