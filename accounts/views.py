from django.shortcuts import render, redirect
from django.views import View
from .models import User, OtpCode
from django.contrib import messages
from .forms import UserRegistrationForm, VerifyCodeForm
import random
from utils import send_otp_code


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(10000, 99999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you otp code', 'success')
            return redirect('accounts:verify_code')
        return redirect('home:home')


class UserVerifyCodeView(View):
    form_class = VerifyCodeForm
    template_name = 'accounts/verify.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'], user_session['full_name'],
                                         user_session['password'])
                code_instance.delete()
                messages.success(request , 'you register successfully' , 'success')
                return redirect('home:home')
            else:
                messages.error(request , 'this code is wrong' , 'danger')
                return redirect('accounts:verify_code')
        return redirect('home:home')