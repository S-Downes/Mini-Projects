from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# Create your views here.
def get_posts(request):
    """
    Returns all posts published currently and renders these in a template called blogposts.html
    """
    posts = Post.objects.filter(published_date__lte=timezone.now() ).order_by("-published_date")
    return render(request, "blogposts.html", { "posts": posts } )
    

def post_detail(request, pk):
    """
    Returns all related information for a single post using the ID and renders it in a template called postdetail.html or else returns
    a 404 error
    """
    post = get_object_or_404(Post, pk = pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", { "post": post } )
    
    
def create_or_edit_post(request, pk = None):
    """
    Allows users to interact with the blog through creating or editing existing posts if pk is specified
    """
    post = get_object_or_404(Post, pk = pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance = post)
        
        if form.is_valid():
            post =form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance = post)        
    return render(request, "blogpostform.html", { "form": form } )
        