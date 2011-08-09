from django.db import models
from model_utils.models import TimeStampedModel

class Rsvp(TimeStampedModel):
    invitation_name = models.CharField(max_length=128, verbose_name="Name on invitation")
    dinner_dancing = models.BooleanField("Will you be joining us on November 4th?")
    email = models.EmailField()
    comments = models.TextField(blank=True, null=True)

class DinnerChoice(TimeStampedModel):
    DINNER_CHOICES = (
        (None, "-----"),
        ("salmon", "Sterling Salmon"),
        ("chicken", "Boneless, Skinless Chicken"),
        ("vegitarian", "Vegetarian"),
        ("kids", "Kid's Dinner")
    )
    rsvp = models.ForeignKey(Rsvp)
    name = models.CharField(max_length=64)
    dinner_choice = models.CharField(max_length=16, choices=DINNER_CHOICES, default=None, null=True)
    
    @property
    def email(self):
        return self.rsvp.email