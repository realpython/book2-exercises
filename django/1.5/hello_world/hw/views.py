from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse('<html><body>Hello, World!</body></html>')

def better(request):
    t = loader.get_template('betterhello.html')
    c = Context({'current_time': datetime.now(),})
    return HttpResponse(t.render(c))
