from django.db.models.signals import pre_save
from django.dispatch import receiver
from info.models import Country
@receiver(pre_save, sender=Country)
def validate_country(sender, instance, **kwargs):
    print("*"*20)
    print("validation called")