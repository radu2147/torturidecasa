from django.shortcuts import redirect

# Create your views here.
def corect(request):
    if request.user.nume == 'bla':
        request.user.nume = request.user.username
        request.user.save()
        return redirect("/")
    return redirect("/")