from django.shortcuts import render, get_object_or_404
from django.urls import reverse 
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post, Comment, Country
from .forms import CommentForm, PostForm, EditPostForm
from django.template.defaultfilters import slugify
from .utils import custom_title_function
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
        country = self.kwargs['country']
        country = custom_title_function(country.replace('-', ' '))
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


def edit_comment(request, country, slug, comment_id):
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


def delete_comment(request, country, slug, comment_id):

    queryset = Post.objects.filter(status=0)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()

    return HttpResponseRedirect(reverse('post_detail', args=[country, slug]))


def add_post(request):

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


def delete_post(request, country, slug, id):

    queryset = Post.objects.filter(status=0)
    post = get_object_or_404(queryset, pk=id)

    if post.author == request.user:
        post.delete()

    return HttpResponseRedirect(reverse('home'))


def edit_post(request, country, slug, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post_form = EditPostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid() and post.author == request.user:
            post.save()

        return HttpResponseRedirect(reverse('post_detail', args=[country, slug]))
    
    else:
        post_form = EditPostForm(instance=post)
        context = {'post_form': post_form, 'id': id, 'post': post}
        return render(request,'website/edit_post.html',context)


class SearchView(generic.TemplateView):
    model = Post
    template_name = 'website/search_results.html'
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('search_term', '')
        # Filter posts by destination name containing the search term
        posts = Post.objects.filter(destination_name__icontains=search_term, status=0)

        # Use Paginator to paginate the queryset
        paginator = Paginator(posts, self.paginate_by)
        page = request.GET.get('page')

        try:
            # Get the requested page
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the page parameter is not an integer, show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the requested page is out of range, show the last page
            posts = paginator.page(paginator.num_pages)

        # Render the template with the paginated posts and search term
        context = {'posts': posts, 'search_term': search_term}
        return render(request, self.template_name, context)