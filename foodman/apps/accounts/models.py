
from django.contrib.auth.models import User
from django.db import models


def upload_to(instance, filename):
    return 'images/%s/%s' % (instance.user.username, filename)

class Avatar(models.Model):
    avatar = models.ImageField(upload_to=upload_to, null=True, blank=True)
    user = models.ForeignKey(User)
    url = models.URLField(max_length=500, null=True, blank=True)

    @property
    def avatar_url(self):
        return (self.avatar.url if self.avatar else None ) or self.url

    def __unicode__(self):
        return u'Avatar for: %s.' % self.user.username
