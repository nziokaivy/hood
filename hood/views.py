from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def home(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request,'index.html')


def my_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)
    
    return render(request,'profile.html',{"profile":profile})

    