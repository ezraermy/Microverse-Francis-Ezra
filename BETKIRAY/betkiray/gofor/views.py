from django.shortcuts import render
from .gofor import Gofor

# Create your views here.
def gofor_detail(request):
    gofor = Gofor(request)
    akeraysstring = ''

    for item in gofor:
        akeray = item['akeray']
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s'}," % (akeray.id, akeray.title, akeray.price, item['quantity'])

        akeraysstring = akeraysstring + b

    context = {
        'gofor': gofor,
        'akeraysstring': akeraysstring
    }

    return render(request, 'gofor.html', context)