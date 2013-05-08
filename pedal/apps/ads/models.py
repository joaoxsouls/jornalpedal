from django.db import models
from django.utils.translation import ugettext as _


class Ad(models.Model):

    name = models.CharField(_('name'), max_length=200)
    image = models.ImageField(upload_to='ads/')
    url = models.URLField()
    highlight = models.BooleanField(_('highlight'))

    def __unicode__(self):
        return self.name
