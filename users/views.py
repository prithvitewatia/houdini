from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from blog.models import Post
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}. You can now login')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    context = {
        'Title': 'Houdini Register',
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request, username: str):
    template_name = ''
    context = {}
    try:
        profile_holder = User.objects.get(username=username)  # Profile holder is a user object
        posts = Post.objects.filter(author__username=username).order_by('-date_posted')
        template_name = 'users/profile.html'
        context = {
            'Title': f'{username} Profile ',
            'profile_holder': profile_holder,
            'posts': posts
        }
    except ObjectDoesNotExist:
        template_name = 'PageNotFound.html'
        context = {
            'Title': 'Page not found'
        }
    finally:
        return render(request, template_name, context=context)


class UserPostListView(ListView):
    model = Post
    template_name = 'users/user_posts.html'
    context_object_name = 'posts'
    paginate_by = '10'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


@login_required
def settings(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Account Updated successfully')
            return redirect('users-profile', username=request.user.username)
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'Title': 'Settings',
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    return render(request, 'users/settings.html', context=context)
