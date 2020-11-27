from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.contrib import messages
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.db.models import Q

from .models import Post
from .form import PostForm, CommentForm


def index_view(request):
    post_list = Post.objects.all()
    query = request.GET.get("q")
    if query:
        post_list = post_list.filter(Q(title__icontains=query) |
                                     Q(content__icontains=query) |
                                     Q(user__first_name__icontains=query) |
                                     Q(user__last_name__icontains=query)
                                     ).distinct()

    paginator = Paginator(post_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts": posts
    }
    return render(request, "post/post_index.html", context)


def details_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        "post": post,
        "form": form
    }
    return render(request, "post/post_details.html", context)


def create_view(request):
    if not request.user.is_authenticated:
        return Http404()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()

        messages.success(request, "Gönderi başarıyla oluşturuldu.", extra_tags="message_succes")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        "form": form
    }
    return render(request, "post/form.html", context)


def update_view(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Gönderi başarıyla güncellendi.", extra_tags="message_succes")
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "post/form.html", context)


def delete_view(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect("post:index_url")
