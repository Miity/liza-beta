from .models import Menu

def menu(request):
    menu_title = Menu.objects.filter(status=True,)
    return {'menu_title':menu_title}