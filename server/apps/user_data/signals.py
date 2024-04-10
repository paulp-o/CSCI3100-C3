from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserData


@receiver(post_save, sender=User)
def create_or_update_user_data(sender, instance, created, **kwargs):
    if created:
        UserData.objects.create(user=instance)
    else:
        instance.userdata.save()


@receiver(pre_delete, sender=User)
def delete_user_data(sender, instance, **kwargs):
    try:
        instance.userdata.delete()
    except UserData.DoesNotExist:
        pass
