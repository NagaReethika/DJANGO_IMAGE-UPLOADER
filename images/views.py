from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import UploadedImage
from .forms import ImageUploadForm

def home_auth_view(request):
    """
    Landing page handling both Sign In and Sign Up entry points.
    If already logged in, redirects directly to the workspace.
    """
    if request.user.is_authenticated:
        return redirect('gallery')

    login_form = AuthenticationForm()
    signup_form = UserCreationForm()

    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'login':
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('gallery')
            else:
                messages.error(request, "Invalid authentication credentials.")
                
        elif action == 'signup':
            signup_form = UserCreationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                messages.success(request, "Account provisioned successfully!")
                return redirect('gallery')
            else:
                messages.error(request, "Registration invalid. Please correct errors.")

    context = {
        'login_form': login_form,
        'signup_form': signup_form
    }
    return render(request, 'images/auth.html', context)

@login_required(login_url='home')
def gallery_view(request):
    search_query = request.GET.get('search', '').strip()
    
    # Filter images to only show the ones uploaded by anyone, or filter down
    if search_query:
        object_list = UploadedImage.objects.filter(Q(title__icontains=search_query))
    else:
        object_list = UploadedImage.objects.all()

    paginator = Paginator(object_list, 6)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    form = ImageUploadForm()
    
    context = {
        'page_obj': page_obj,
        'form': form,
        'search_query': search_query
    }
    return render(request, 'images/gallery.html', context)

@login_required(login_url='home')
def upload_image_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image successfully uploaded!")
            return redirect('gallery')
        else:
            messages.error(request, "Upload failed.")
    return redirect('gallery')

@login_required(login_url='home')
def delete_image_view(request, pk):
    if request.method == 'POST':
        target_record = get_object_or_404(UploadedImage, pk=pk)
        target_record.delete()
        messages.warning(request, "Image permanently deleted.")
    return redirect('gallery')

def logout_view(request):
    logout(request)
    messages.info(request, "Session disconnected safely.")
    return redirect('home')