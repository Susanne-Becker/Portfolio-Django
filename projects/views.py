from django.shortcuts import render, redirect
from projects.models import Project, Contact
from django import forms
from projects.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

"""
Als email verstuurd wordt, verstuur het en render pagina.
"""
def project_index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['susannevbecker@hotmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, "project_index.html", {
        "projects": Project.objects.all(),
        "contact": Contact.objects.all(),
        "contactform": ContactForm()
    })

"""
render pagina met informatie
"""
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)
