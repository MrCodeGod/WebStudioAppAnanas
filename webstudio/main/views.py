from django.conf import settings
from django.shortcuts import render
from .models import Content
from django.core.mail import send_mail
from django.template import loader


def index(request):
    contents = Content.objects.order_by('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        number = request.POST.get('tel')
        html_message = loader.render_to_string('main/msg.html', {'name': name, 'age': age, 'email': email, 'number': number})
        send_mail(
            subject='Новая заявка!',
            message=html_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['nekit.ostroushko@mail.ru'],
            fail_silently=False,
        )
    return render(request, 'main/index.html', {'contents': contents})