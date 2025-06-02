from .models import PostCategory

def categories(request):
    return {'categories': PostCategory.objects.all()}