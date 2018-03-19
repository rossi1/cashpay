from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender=settings.TOKEN_MODEL)
def save_profile(sender, instance, created):
    if created:
        instance.status.check_stat = True
        if hasattr(instance.status, 'save'):
            instance.status.save()
