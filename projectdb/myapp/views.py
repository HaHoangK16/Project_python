from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Staff
from myapp.models import Store

# Create your views here.
#def home(request):
    #return HttpResponse("SQLlife")
#     rs = Staff.objects.all()
#     s = ""
#     for item in rs:
#         s = s + "ID: " + str(item.id) + ", Name: " \
#             + str(item.fullname) + ", Sex: " \
#             + str(item.sex) + ", Age: " \
#             + str(item.age) + ", Address: " \
#             + str(item.address) + "</br>"
#     return HttpResponse(s)
#
# def home(request):
#     rx = Store.objects.all()
#     x = ""
#     for item in rx:
#         x = x + "ID: " + str(item.id) + ", Name: " \
#             + str(item.storename) + ", Phone: " \
#             + str(item.phone) + ", Address: " \
#             + str(item.storeaddress) + "</br>"
#     return HttpResponse(x)


def home(request):
    rs = Staff.objects.all()
    context = {
        'rs': rs,
    }
    return render(request, 'pages/display_page01.html', context)
