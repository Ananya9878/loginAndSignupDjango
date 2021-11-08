from django.shortcuts import render

# Create your views here.
def home(request):
    user = request.user
    context = {}
    if user.username == 'AnonymousUser':
        context['user'] = ''
    else:
        context['user'] = user.username
    return render(request, "home.html",context=context)

