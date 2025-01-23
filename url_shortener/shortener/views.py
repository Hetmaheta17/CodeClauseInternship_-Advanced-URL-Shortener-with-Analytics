from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.crypto import get_random_string
from .models import ShortenedURL, Analytics
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    urls = ShortenedURL.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'urls': urls})


@login_required
def create_short_url(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_url = get_random_string(length=6)  
        ShortenedURL.objects.create(user=request.user, original_url=original_url, short_url=short_url)
        return redirect('dashboard')

    return render(request, 'create_url.html')

def redirect_url(request, short_url):
    try:
        shortened_url = ShortenedURL.objects.get(short_url=short_url)
        shortened_url.click_count += 1
        shortened_url.save()

        # Log the click in Analytics
        Analytics.objects.create(shortened_url=shortened_url)

        return HttpResponseRedirect(shortened_url.original_url)
    except ShortenedURL.DoesNotExist:
        return HttpResponse("URL not found.", status=404)

def home(request):
    return render(request, 'home.html')


@login_required
def delete_short_url(request, short_url):
    # Get the URL to delete
    shortened_url = get_object_or_404(ShortenedURL, short_url=short_url, user=request.user)
    
    # Delete the URL
    shortened_url.delete()
    return redirect('dashboard')  