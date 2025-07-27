from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            send_mail(
                subject=f"New Contact: {form.cleaned_data['subject']}",
                message=f"From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n{form.cleaned_data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact/success.html')