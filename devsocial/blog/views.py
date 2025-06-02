from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post , PostCategory
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm 

def homepage(request):
    post_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/homepage.html', {'page_obj': page_obj})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:profile')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:profile')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update_post.html', {'form': form, 'post': post})

@login_required
def profile(request):
    user_posts = request.user.posts.all().order_by('-created_at')
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/profile.html', {'page_obj': page_obj})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Allow if user is author or user is staff (custom role)
    can_delete = (post.author == request.user) or (
        request.user.role and request.user.role.role == 'staff'
    )
    if not can_delete:
        return redirect('blog:homepage')
    if request.method == 'POST':
        post.delete()
        return redirect('blog:profile' if post.author == request.user else 'blog:homepage')
    return render(request, 'blog/delete_post.html', {'post': post})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def category_posts(request, category_id):
    category = get_object_or_404(PostCategory, id=category_id)
    post_list = Post.objects.filter(category=category).order_by('-created_at')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/category_posts.html', {
        'category': category,
        'page_obj': page_obj,
    })