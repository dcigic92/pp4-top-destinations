from django.shortcuts import render, get_object_or_404
from django.urls import reverse 
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post, Comment, Country
from .forms import CommentForm, PostForm
from django.template.defaultfilters import slugify


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=0)
    template_name = "website/index.html"
    paginate_by = 3


class CountryPostsView(generic.ListView):
    model = Post
    template_name = 'website/country_posts.html'
    paginate_by = 3

    def get_queryset(self):
        country = self.kwargs['country'].capitalize()
        country_id = Country.objects.get(name=country)
        return Post.objects.filter(country_of_destination=country_id.id)


def post_detail(request, country, slug):
    
    queryset = Post.objects.filter(status=0)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(status=0).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    comment_form = CommentForm()

    return render(
        request, 
        "website/post_detail.html", 
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, country, slug, comment_id):
    if request.method == "POST":

        queryset = Post.objects.filter(status=0)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.status = 0
            comment.save()

    return HttpResponseRedirect(reverse('post_detail', args=[country, slug]))


def comment_delete(request, country, slug, comment_id):

    queryset = Post.objects.filter(status=0)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()

    return HttpResponseRedirect(reverse('post_detail', args=[country, slug]))


def add_destination(request):

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.destination_name)
            post.save()

    post_form = PostForm()

    if request.method == "POST":
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(
            request, 
            "website/add_post.html", 
            {
                "post_form": post_form,
            },
        )