from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, AddHoodForm
from .models import Business, Profile, Join, Neighbourhood

def index(request):
    title = 'Home'
    return render(request, 'index.html', {'title':title})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})

@login_required
def create_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return redirect('/')

    else:

        form = ProfileForm()
    return render(request,'user/profile_form.html',{"form":form})

login_required
def home(request):
    if Join.objects.filter(user_id=request.user).exists():
        hood = Neighbourhood.objects.get(pk=request.user.join.hood_id.id)
        posts = Post.objects.filter(post_hood=request.user.join.hood_id.id)
        businesses = Business.objects.filter(business_hood=request.user.join.hood_id.id)
        return render(request, 'current_hood.html', {"hood": hood, "businesses": businesses, "posts": posts})
    else:
        hoods = Neighbourhood.all_neighborhoods()
    return render(request, 'hood/home.html', {"hoods": hoods})

@login_required
def add_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user_profile = current_user
            hood.save()
        return redirect('home')

    else:
        form = AddHoodForm()
    return render(request, 'hood/add_hood.html', {"form": form})
