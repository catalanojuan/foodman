
import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


def upload_to(instance, filename):
    return 'images/%s/%s' % (instance.user.username, filename)

class Avatar(models.Model):
    avatar = models.ImageField(upload_to=upload_to)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'Avatar for: %s.' % self.user.username
