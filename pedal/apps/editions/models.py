from django.db import models
from django.utils.translation import ugettext as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Edition(models.Model):

    MONTH_CHOICES = ((1, _('January')), (2, _('February')), (3, _('Mars')), (4, _('April')), (5, _('May')),
                     (6, _('June')), (7, _('July')), (8, _('August')), (9, _('September')),
                     (10, _('October')), (11, _('November')), (12, _('December')))

    YEAR_CHOICES = ((2012, 2012), (2013, 2013), (2014, 2014))

    number = models.IntegerField(_('number'))
    month = models.IntegerField(choices=MONTH_CHOICES)
    year = models.IntegerField(choices=YEAR_CHOICES)
    image = models.ImageField(upload_to='editions/')
    thumbnail = ImageSpecField([ResizeToFill(width=235, height=300)], image_field='image', format='PNG', cache_to='editions/thumbs')
    file = models.FileField(_('file'), upload_to='editions/files/')
    highlight = models.BooleanField(_('highlight'))

    def __unicode__(self):
        return self.get_month_display()

    class Meta:
        verbose_name = _('Edition')
