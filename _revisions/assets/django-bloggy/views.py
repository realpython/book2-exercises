from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render, redirect

from blog.models import Post
from blog.forms import PostForm


####################
# helper functions #
####################

def get_popular_posts():
    popular_posts = Post.objects.order_by('-views')[:5]
    return popular_posts


##################
# view functions #
##################

def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')
    t = loader.get_template('blog/index.html')
    context_dict = {
        'latest_posts': latest_posts,
        'popular_posts': get_popular_posts(),
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def post(request, slug):
    single_post = get_object_or_404(Post, slug=slug)
    single_post.views += 1  # increment the number of views
    single_post.save()      # and save it
    t = loader.get_template('blog/post.html')
    context_dict = {
        'single_post': single_post,
        'popular_posts': get_popular_posts(),
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  # is the form valid?
            form.save(commit=True)  # yes? save to database
            return redirect(index)
        else:
            print(form.errors)  # no? display errors to end user
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})
