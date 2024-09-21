from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Senior
from django.contrib import messages
#from .models import SearchSenior
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from . forms import CreateUserForm, SeniorForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def base(request):
    return render(request, 'senior_data/base.html')

@login_required
def search_senior(request):
    searched = request.GET.get('searched', '')
    seniors = Senior.objects.filter(full_name__contains=searched)
    return render(request, 'senior_data/search-results.html', {'searched': searched, 'seniors':seniors})

@login_required
def get_items(request, pk):
    items = Senior.objects.filter(pk=pk)
    return render(request, 'senior_data/senior-detail.html', {'items': items})

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for ' + user)
            return redirect('login')
        form = CreateUserForm()
    return render(request, 'senior_data/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list')  # Replace with the URL name of the view you want to redirect to after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'senior_data/login.html', {'form': form})

@login_required
def add_senior(request):
    if request.method == 'POST':
        form = SeniorForm(request.POST, request.FILES)
        if form.is_valid():
            senior = form.save(commit=False)
            senior.user = request.user  # Automatically assign the current user to the senior
            senior.save()
            return redirect('list')  # Redirect to a success page or another view
    else:
        form = SeniorForm()
    return render(request, 'senior_data/add-senior.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('index')


def index_view(request):
    return render(request, 'senior_data/index.html')


class SeniorListView(LoginRequiredMixin, ListView):
    model = Senior
    login_url = reverse_lazy('login')
    template_name = "senior_data/senior-list.html"
    context_object_name = "senior"


class SeniorDetailView(LoginRequiredMixin, DetailView):
    model = Senior
    login_url = reverse_lazy('login')
    template_name = "senior_data/senior-detail.html"
    context_object_name = "senior_detail"


@login_required
def delete_senior(request, pk):
    senior = get_object_or_404(Senior, pk=pk)
    if request.method == 'POST':
        senior.delete()
        messages.success(request, 'Senior deleted successfully.')
        return redirect('list')  # Redirect to the list view or another page
    return render(request, 'senior_data/senior-detail.html', {'senior': senior})