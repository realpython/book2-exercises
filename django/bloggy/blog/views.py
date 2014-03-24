from django.http import HttpResponse
from blog.models import Post
from django.template import Context, loader     
from django.shortcuts import get_object_or_404

def index(request):
   latest_posts = Post.objects.all().order_by('-created_at')
   t = loader.get_template('index.html')
   c = Context({'latest_posts': latest_posts,})
   return HttpResponse(t.render(c))

def post(request, post_id):
    single_post = get_object_or_404(Post, pk=post_id)
    t = loader.get_template('post.html')
    c = Context({'single_post': single_post,})
    return HttpResponse(t.render(c))
