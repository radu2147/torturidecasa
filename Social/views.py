from django.shortcuts import redirect
from User.models import Address

# Create your views here.
def corect(request):
    if request.user.nume == 'bla':
        request.user.nume = request.user.username
        request.user.save()
        if request.user.addr == None:
            adr = Address.objects.create(street="", phone_number="", scara="")
            request.user.addr = adr
            request.user.save()

    return redirect("/")