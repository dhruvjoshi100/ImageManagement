from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


#for authentication
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class MyPhoto(models.Model):
    image = models.ImageField(upload_to='photos', max_length=254)
    owner = models.ForeignKey('auth.User', related_name='image')
	

    