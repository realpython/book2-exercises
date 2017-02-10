from .forms import ContactView
from django.contrib import messages
from django.shortcuts import render, redirect


def contact(request):
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            our_form = form.save(commit=False)
            our_form.save()
            messages.add_message(
                request, messages.INFO, 'Your message has been sent. Thank you.'
            )
            return redirect('/')
    else:
        form = ContactView()
    return render(request, 'contact.html', {'form': form, })
