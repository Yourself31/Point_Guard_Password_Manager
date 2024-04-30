from django.shortcuts import render, redirect
from .models import UserPassword, PasswordCategory  # Adjusted import to match the application's context
from .forms import UserPasswordForm, PasswordCategoryForm

# Create your views here.
# def home(request):
#     # Retrieve all password categories sorted by name
#     password_categories = PasswordCategory.objects.all().order_by('name')
#     # Render the page with the information about the password categories
#     return render(request, 'content/home.html', {'password_categories': password_categories})

def home(request):
    if request.user.is_authenticated:
        user_passwords = UserPassword.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'content/home.html', {'user_passwords': user_passwords})
    else:
        return render(request, 'content/home.html', {'message': 'Please log in to view passwords.'})
    
    
def add_password_category(request):
    if request.method == 'POST':
        form = PasswordCategoryForm(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.user = request.user  # Assuming categories are user-specific
            new_category.save()
            return redirect('content/home.html')  # Redirect to a relevant page
    else:
        form = PasswordCategoryForm()

    return render(request, 'content/add_password_category.html', {'form': form})

def add_password(request):
    # Upon submission, retrieve and save the form data if it is valid. Then redirect to the home page.
    if request.method == 'POST':
        form = UserPasswordForm(request.POST)
        if form.is_valid():
            # Assuming you want to associate this password with the current user
            user_password = form.save(commit=False)
            user_password.user = request.user
            user_password.save()
            return redirect('home')  # Ensure 'home' is the name of your homepage URL pattern
    # Otherwise, initialize the form and render the page to allow data entry
    else:
        form = UserPasswordForm()
    return render(request, 'content/add_password.html', {'form': form})
