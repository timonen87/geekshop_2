from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


import hashlib
import random
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver





class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default= '18')

    is_delete = models.BooleanField(default=False)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))


    def save(self, *args, **kwargs):
        if not self.pk:
            # not created now
            self.activated = False
            salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]

            self.activation_key = hashlib.sha1((self.email + salt).encode('utf8')).hexdigest()
            self.activation_key_expires = now() + timedelta(hours=48)
            
            # send activated email
            send_mail(
                'Email from django',
                f"""Активируйте свой аккаунт http://127.0.0.1:8000/auth/activate/{self.activation_key}""",
                settings.EMAIL_HOST_USER,
                [self.email],
                fail_silently=False
            )
        super().save(*args, **kwargs)


    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'М'),
        ('W', 'Ж'),
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)

    tagline = models.CharField(verbose_name='теги', max_length=128,  blank=True)
    about_me = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=user)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)


    @receiver(post_save, sender=user)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

