from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Business, Profile, Neighbourhood, News, Health, Authorities
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    try:
        if not request.user.is_authenticated:
            return redirect('accounts/login/')
        user=request.user
        profile =Profile.objects.get(username=user)
    except ObjectDoesNotExist:
        return redirect('create_profile')

    return render(request,'index.html')


def my_profile(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    return render(request,'my_profile.html',{"profile":profile})


def create_profile(request):
    current_user = request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:

        form = ProfileForm()
    return render(request,'create_profile.html',{"form":form})

def businesses(request):
    current_user = request.user
    business = Business.objects.order_by('-pub_date')
    return render(request, 'business.html', {'business':business})

def health(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    healthservices = Health.objects.filter(neighbourhood_id=profile.neighbourhood)

    return render(request,'health.html',{"healthservices":healthservices})

def authorities(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    authorities = Authorities.objects.filter(neighbourhood_id=profile.neighbourhood)

    return render(request,'authorities.html',{"authorities":authorities})