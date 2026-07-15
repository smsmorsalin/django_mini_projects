from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))  # Redirect to a success page
        else:
            return render(request, 'login.html', {
                'message': 'Invalid username or password. Please try again.'
            })
    return render(request, 'login.html')  # Render the login page for GET requests

def log_out(request):
    if request.method == 'POST':
        # Handle logout logic here
        logout(request)
        return render(request, 'login.html', {
            'message': 'You have been logged out successfully.'
        })  # Redirect to the login page
    return render(request, 'users/logout.html')