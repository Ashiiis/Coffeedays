from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from coffeeshop import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from django.db import models
# Create your views here.
def home(request):
    return render(request, "authint/index.html")

# class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    signup_confirmation = models.BooleanField(default=False)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    signup_confirmation = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=20, blank=True, null=True)

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        number = request.POST['number']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        address = request.POST.get('address', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        pin_code = request.POST.get('pin_code', '')
        

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.save()

        # profile = Profile.objects.create(
        #     user=myuser,
        #     signup_confirmation=False,
        #     address=address,
        #     state=state,
        #     country=country,
        #     pin_code=pin_code
        # )
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('coffee/home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('coffee/home')
        
        if User.objects.filter(number=number).exists():
            messages.error(request, "number Already Registered!!")
            return redirect('coffee/home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('coffee/home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('coffee/home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('coffee/home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        #myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to GFG- Django Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('signin')
        
        
    return render(request, "authint/signup.html")


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        #User.profile.signup_confirmation = True
        myuser.profile.signup_confirmation = True

        myuser.profile.save()
        login(request,myuser)

        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "/",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('coffee/home')
    
    return render(request, "authint/signin.html")
 

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('coffee/home')