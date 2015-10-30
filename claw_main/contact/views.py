# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.conf import settings
from django.core.mail import send_mail
# from django.contrib import messages

from .forms import ContactView


# Create your views here.
def contact(request):
    """TODO: Docstring for contact.
    :returns: TODO

    """
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data.get('name')
            form_email = form.cleaned_data.get('email')
            form_topic = form.cleaned_data.get('topic')
            form_message = form.cleaned_data.get('message')
            subject = 'Site contact form'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, 'ppilipovic84@gmail.com']
            contact_message = "%s: %s%s via %s" % (
                form_name,
                form_email,
                form_topic,
                form_message)
            send_mail(subject,
                      contact_message,
                      from_email,
                      to_email,
                      fail_silently=False)
#            our_form = form.save(commit=False)
#            our_form.save()
#            messages.add_message(
#                request, messages.INFO,
#                'Your message has been sent. Thank you.'
#            )
            return HttpResponseRedirect('/')
    else:
        form = ContactView()
    t = loader.get_template('contact.html')
    c = RequestContext(request, {'form': form, })
    return HttpResponse(t.render(c))
