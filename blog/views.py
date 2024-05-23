from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from slugify import slugify


# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


class UserPostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/user_posts.html"

    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        return queryset


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    like_count = post.likes.filter().count()
    unlike_count = post.unlikes.filter().count()
    comments = post.comments.all().order_by("-created_on")
    liked = post.likes.filter(id=request.user.id).exists()
    unliked = post.unlikes.filter(id=request.user.id).exists()
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment submitted and awaiting approval')

    comment_form = CommentForm()

    return render(
     request,
     "blog/post_detail.html",
     {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        'liked': liked,
        'unliked': unliked,
        "unlike_count": unlike_count,
        "like_count": like_count
     },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def add_post(request,):
    post_form = PostForm()
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
        post = post_form.save(commit=False)
        post.author = request.user
        post.slug = slugify(post.title)
        post.status = 1
        post_form.save()
        messages.add_message(request, messages.SUCCESS,
                             "Post created successfully ")
        return HttpResponseRedirect(reverse('home'))
    # addpost = AddPost.objects.all().order_by('-updated_on').first()

    post_form = PostForm()
    return render(request, "blog/add_post.html", {"post_form": post_form},
                  )


def post_edit(request, post_id):
    """
    view to edit post
    """
    post = get_object_or_404(Post, pk=post_id)
    post_form = PostForm(instance=post)
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES, instance=post)
    if post_form.is_valid() and post.author == request.user:
        post = post_form.save(commit=False)
        post.post = post
        post.approved = False
        post.save()
        messages.add_message(request, messages.SUCCESS,
                             'Post Updated!')
        return HttpResponseRedirect(reverse('post_detail',
                                    args=[post.slug]))
    else:
        return render(
         request,
         "blog/post_edit.html", {"post_form": post_form, "post": post},
        )


def post_delete(request, post_id):
    """
    view to delete post
    """
    # Fetch the post object using the post_id,
    # or return a 404 error if it doesn't exist
    post = get_object_or_404(Post, id=post_id)

    # Check if the current user is the author of the post
    if request.user == post.author:
        # If the request method is POST,
        # it means the user has confirmed the deletion
        if request.method == 'POST':
            # Delete the post
            post.delete()
            messages.add_message(request, messages.SUCCESS,
                                 'Post deleted!')
            # Redirect the user to a relevant page, e.g., the homepage
            return HttpResponseRedirect(reverse('home'))
        # If the request method is not POST, render a confirmation template
        else:
            return render(request, 'blog/post_delete.html',
                          {'post': post})


def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            if request.user not in post.likes.all():
                post.unlikes.remove(request.user)
                post.likes.add(request.user)
                post.save()
        return HttpResponseRedirect(reverse('post_detail',
                                    args=[post.slug]))
    else:
        return JsonResponse({'status': 'error', 'message':
                            'Only POST requests are allowed'})


def post_unlike(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        if request.user in post.unlikes.all():
            post.unlikes.remove(request.user)
        else:
            if request.user not in post.unlikes.all():
                post.likes.remove(request.user)
                post.unlikes.add(request.user)
                post.save()

        return HttpResponseRedirect(reverse('post_detail',
                                    args=[post.slug]))
    else:
        return JsonResponse({'status': 'error', 'message':
                            'you liked this post, unable to unlike'})
