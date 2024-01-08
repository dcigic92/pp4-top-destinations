from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=0)
    template_name = "website/index.html"
    paginate_by = 3

def post_detail(request, slug):
    
    queryset = Post.objects.filter(status=0)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(status=0).count()
    return render(
        request, 
        "website/post_detail.html", 
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
        },
    )