from django.shortcuts import render
from .models import Test

def TestPage(request):
    testObjects = Test.objects.all()
    return render(request, 'blog/testPage.html', {'testObjects':testObjects} )

@login_required
def profile(request):
    user_posts = request.user.posts.all().order_by('-created_at')
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/profile.html', {'page_obj': page_obj})