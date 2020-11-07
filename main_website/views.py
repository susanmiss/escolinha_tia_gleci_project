from django.shortcuts import render, redirect
from .models import School, Diferentials, Visitation, Footer
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, ContactFormHome
from django.core.mail import send_mail, BadHeaderError




def home(request):
    footers = Footer.objects.all()
    if request.method == 'POST':
        form = ContactFormHome(request.POST)
        if form.is_valid():

            sender_name = form.cleaned_data['name']

            sender_phone = form.cleaned_data['phone']

            sender_email = form.cleaned_data['email']

            message = "{0}, numero telefonico {1}, from email {2} requisita que voce entre em contato por telefone ou e-mail".format(sender_name, sender_phone, sender_email)

            send_mail('Nova Mensagem pelo website Site Escolinha Tia Gleci', message, sender_email, ['fsusan@icloud.com'])
            
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'main_website/home.html', {'footers': footers})

def school(request):
    schools = School.objects.all()
    footers = Footer.objects.all()
    return render(request, 'main_website/school.html', {'schools': schools, 'footers': footers})

def diferentials(request):
    diferentials = Diferentials.objects.all()
    footers = Footer.objects.all()
    return render(request, 'main_website/diferentials.html', {'diferentials': diferentials, 'footers': footers})    

def visitation(request):
    visitations = Visitation.objects.all()
    footers = Footer.objects.all()
    return render(request, 'main_website/visitation.html', {'visitations': visitations, 'footers': footers}) 

def success(request):
    footers = Footer.objects.all()
    return render(request, 'main_website/success.html', {'footers': footers})   


def contact_us(request):
    footers = Footer.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            sender_name = form.cleaned_data['name']

            sender_phone = form.cleaned_data['phone']
  
            sender_email = form.cleaned_data['email']

            message = "{0}, numero telefonico {1}, enviou uma nova mensagem:\n\n{2}".format(sender_name, sender_phone, form.cleaned_data['message'])

            send_mail('Nova Mensagem pelo website Site Escolinha Tia Gleci', message, sender_email, ['fsusan@icloud.com'])

            # return HttpResponseRedirect('contact_us', 'You message')
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'main_website/contact_us.html', {'form': form, 'footers': footers})

