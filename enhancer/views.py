from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def browse(request):
    return render(request, 'browse.html')

def streams(request):
    return render(request, 'streams.html')
