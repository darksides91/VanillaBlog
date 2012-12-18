from django.db import models
from django.utils.translation import ugettext_lazy as _

class Poll(models.Model):
    title = models.CharField(_(u'title'), max_length=254)
    question = models.TextField(_(u'content'))
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return u'Poll %s : %s' % (self.title, self.question)
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()