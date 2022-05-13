from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView,CreateView, FormView
from vote import models as voteModels
from vote import forms as voteForms
from django.contrib.auth.models import User
from django.contrib import messages

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from vote.token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

def entry_code_generator():
    """
    this is the entry code generator. 
    It uses random and checks for the database. 
    return the code if it's not taken
    """
    import random
    code  = str(random.choice('abcdefghijklmnpqrstuvwxyz'))
    code += str(random.randint(1,9))
    code += str(random.choice('abcdefghijklmnpqrstuvwxyz'))
    code += str(random.randint(1,9))
    code += str(random.choice('abcdefghijklmnpqrstuvwxyz'))
    code = code.upper()
    is_exist = User.objects.filter(username = code).exists()
    
    if is_exist:
        entry_code_generator()
    return code


def ClainYourSeat(request):
    """this is the user creation function. It create a user and assign entry code and relevent info"""
    form = voteForms.ClaimYourSeatForm()
    if request.method == 'POST':
        form = voteForms.ClaimYourSeatForm(request.POST or None)
        if form.is_valid():
            # set the username to 5 digit random unique and set password
            user = form.save(commit=False)
            user.username = entry_code_generator()
            user.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()

            user.users.legalName = form.cleaned_data.get('legalName')
            user.users.address = form.cleaned_data.get('address')
            usersDistrict = voteModels.Districts.objects.get(code = form.cleaned_data.get('district').upper())
            if usersDistrict:
                user.users.district = usersDistrict
                
            user.save()
            messages.success(
                request,
                "We've sent an email to the address you provided. Open it and click on the link to confirm and Enter the Floor.",
                extra_tags='success' 
            )

            # send email
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('vote/accountActiveEmail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = user.email
            email = EmailMessage( mail_subject,  message,  to=[to_email] )
            email.send()

            # redirect to confirmation page
            return render(request, 'vote/signUpConfirm.html')
        else:
            return render(request, 'vote/ClaimYourSeat.html',{'form':form})
    return render(request, 'vote/ClaimYourSeat.html',{'form':form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        users = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        users = None
    if users is not None and account_activation_token.check_token(users, token):
        users.is_active = User.objects.filter(id=uid).update(is_active=True)
        login(request, users)
        messages.success(request,"Successfully Registered and Activated.")
        return render(request, 'vote/index.html')
    else:
        return HttpResponse('Activation link is invalid!')

        
class EnterTheFloor(CreateView):
    model = voteModels.Users
    fields = ['district']
    template_name = 'vote/EnterTheFloor.html'

