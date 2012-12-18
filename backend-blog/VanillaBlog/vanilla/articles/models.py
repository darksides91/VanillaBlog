from django.db import models
from django.utils.translation import ugettext_lazy as _

class Article(models.Model):
    title = models.CharField(_(u'title'), max_length=254)
    content = models.TextField(_(u'content'))
    author = models.CharField(max_length=128)

    def __unicode__(self):
        return u'Article %d : %s' % (self.id, self.title)
