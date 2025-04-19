from django.shortcuts import render
from .models import Test

def TestPage(request):
    testObjects = Test.objects.all()
    return render(request, 'blog/testPage.html', {'testObjects':testObjects} )

