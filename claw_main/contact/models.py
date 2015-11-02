from django.db import models
import datetime


# Create your models here.
class ContactForm(models.Model):

    """Docstring for ContactForm. """
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=250)
    topic = models.CharField(max_length=150)
    message = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.email

    class Meta:
        ordering = ['-timestamp']
