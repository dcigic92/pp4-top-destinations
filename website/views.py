from django.shortcuts import render, get_object_or_404
from django.urls import reverse 
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post, Comment, Country
from .forms import CommentForm, PostForm, EditPostForm
from django.template.defaultfilters import slugify
from .utils import custom_title_function
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# PostList view, which inherits from Django's generic ListView class
class PostList(generic.ListView):
    # Set the model to Post
    model = Post
    # Set the queryset to all posts that have been published
    queryset = Post.objects.filter(status=0)
    # Set the template name to index.html
    template_name = "website/index.html"
    # Set the number of posts per page to 3
    paginate_by = 3


# CountryPostsView view, which inherits from Django's generic ListView class
class CountryPostsView(generic.ListView):
    # Set the model to Post
    model = Post
    # Set the template name to country_posts.html
    template_name = 'website/country_posts.html'
    # Set the number of posts per page to 3
    paginate_by = 3

    # Override the get_queryset method to filter posts by country
    def get_queryset(self, request):
        # Get the country from the URL
        country = self.kwargs['country']
        # Use the custom_title_function to convert the country name to title case
        # and replace "-" with spaces
        country = custom_title_function(country.replace('-', ' '))
        # Try to get the country from the database
        try:
            # If the country exists, filter posts by country
            country_id = Country.objects.get(name=country)
            return Post.objects.filter(country_of_destination=country_id.id)
        except Country.DoesNotExist:
            # If the country does not exist, return an empty queryset
            return Post.objects.none()
        

# PostDetail view, written as a function, which takes the request, country, and slug as parameters 
# and returns the rendered post_detail.html template
def post_detail(request, country, slug):
    # Set the queryset to all posts that have been published
    queryset = Post.objects.filter(status=0)
    # Get the post from the database using the slug
    # If the post does not exist, return a 404 error
    post = get_object_or_404(queryset, slug=slug)
    # Get all comments for the post and order them by the created_on field
    comments = post.comments.all().order_by("-created_on")
    # Get the number of comments for the post
    comment_count = post.comments.filter(status=0).count()

    # Check if the request method is POST
    if request.method == "POST":
        # Create a new comment using the data from the request
        comment_form = CommentForm(data=request.POST)
        # Check if the form is valid
        if comment_form.is_valid():
            # If the form is valid, create a new comment object but do not save it to the database straight away
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    # Create a new blank comment form
    comment_form = CommentForm()

    # Render the post_detail.html template with the post, comments, comment_count, and comment_form
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


# EditComment view, written as a function, which takes the request, country, and slug as parameters
def edit_comment(request, country, slug, comment_id):
    # Get the post from the database using the country and slug
    if request.method == "POST":
        # Get all published posts from the database
        queryset = Post.objects.filter(status=0)
        # If the post does not exist, return a 404 error
        post = get_object_or_404(queryset, slug=slug)
        # Get the comment from the database using the comment_id
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        # Check if the form is valid and user is comment author
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.status = 0
            comment.save()

    # If the request method is GET, create a new blank comment form
    return HttpResponseRedirect(reverse('post_detail', args=[country, slug]))


# DeleteComment view, written as a function, which takes the request, country, and slug as parameters
def delete_comment(request, country, slug, comment_id):
    # Get all published posts from the database
    queryset = Post.objects.filter(status=0)
    # Get the post from the database using the slug
    post = get_object_or_404(queryset, slug=slug)
    # Get the comment from the database using the comment_id
    comment = get_object_or_404(Comment, pk=comment_id)

    # Check if the comment author is the same as the logged in user
    if comment.author == request.user:
        # If the comment author is the same as the logged in user, delete the comment
        comment.delete()

    # Redirect the user to the post_detail page
    return HttpResponseRedirect(reverse('post_detail', args=[country, slug]))


# AddPost view, written as a function, which takes the request as a parameter
def add_post(request):
    # If the request method is POST, create a new post
    if request.method == "POST":
        # Create a new post using the data from the request
        post_form = PostForm(request.POST, request.FILES)
        # Check if the form is valid
        if post_form.is_valid():
            # If the form is valid, create a new post object but do not save it to the database straight away
            post = post_form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.destination_name)
            post.save() # Save

    # Redirect user to home page if method was post
    if request.method == "POST":
        return HttpResponseRedirect(reverse('home'))
    else:
        # Render the add_post.html template with the post_form
        return render(
            request, 
            "website/add_post.html", 
            {
                "post_form": post_form,
            },
        )


# DeletePost view, written as a function, which takes the request, country, slug, and id as parameters
def delete_post(request, country, slug, id):
    
    queryset = Post.objects.filter(status=0)
    # Get the post from the database using the id
    post = get_object_or_404(queryset, pk=id)

    # Check if the post author is the same as the logged in user
    if post.author == request.user:
        post.delete()

    # Redirect the user to the home page
    return HttpResponseRedirect(reverse('home'))


# EditPost view, written as a function, which takes the request, country, slug, and id as parameters
def edit_post(request, country, slug, id):
    # Get the post from the database using the id
    post = get_object_or_404(Post, id=id)

    # Check if the request method is POST
    if request.method == "POST":
        # If the request method is POST, create a new post using the data from the request
        post_form = EditPostForm(request.POST, request.FILES, instance=post)
        # Check if the form is valid and the post author is the same as the logged in user
        if post_form.is_valid() and post.author == request.user:
            # If the form is valid and the post author is the same as the logged in user, save the post
            post.save()

        # Redirect the user to the edited post
        return HttpResponseRedirect(reverse('post_detail', args=[country, slug]))
    
    # If the request method is GET, create a new post form
    else:
        # Render the edit_post.html template with form for editing
        post_form = EditPostForm(instance=post)
        context = {'post_form': post_form, 'id': id, 'post': post}
        return render(request,'website/edit_post.html',context)


# SearchView view, which inherits from Django's generic TemplateView class
class SearchView(generic.TemplateView):
    # Set the model to Post
    model = Post
    # Set the template name to search_results.html
    template_name = 'website/search_results.html'
    # Set the number of posts per page to 3
    paginate_by = 3

    # Override the get method to get the search term from the request
    def get(self, request, *args, **kwargs):
        # Get the search term from the request
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

def custom_404(request, exception):
    return render(request, '404.html', status=404)