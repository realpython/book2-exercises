from django.shortcuts import render
from payments.models import User


def index(request):
    uid = request.session.get('user')
    if uid is None:
        return render(request, 'index.html')
    else:
        return render(
            request,
            'user.html',
            {'user': User.objects.get(pk=uid)}
        )
