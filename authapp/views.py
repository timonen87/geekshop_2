from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm

from django.core.mail import send_mail
from django.conf import settings
from authapp.models import ShopUser



def login(request):
    title = 'входа'

    login_form = ShopUserLoginForm(data=request.POST)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        passsword = request.POST['password']

        user = auth.authenticate(username=username, password=passsword)
        auth.authenticate()
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form,
        'next': next,
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('Сообщение подтверждения отправлено')
            else:
                print('Ошибка отправки сообщения')
        return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = ShopUserRegisterForm()
        content = {'title': title, 'register_form': register_form}
        return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    
    title = f'Подтверждение учетной записи {user.username}'

    message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
    
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
