from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Contact(models.Model):
    user=models.ForeignKey(User,unique=True)
    joined=models.DateField(auto_now=True)
    is_subscriber=models.BooleanField(verbose_name="Subscribe to email blast?", default=False)
    street=models.CharField(max_length=200,blank=True,null=True)
    state=models.CharField(max_length=200,blank=True,null=True)
    zip=models.IntegerField(blank=True,null=True)
    city=models.CharField(max_length=200,blank=True,null=True)
    
    def __unicode__(self):
        return '%s %s' %(self.user.first_name, self.user.last_name)
        
class Subscriber(models.Model):
    email=models.EmailField()
    
    def __unicode__(self):
        return self.email
