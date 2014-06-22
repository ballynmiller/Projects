from django.db import models
from django.conf import settings

import Image

class Section(models.Model):
    name=models.CharField(max_length=20,help_text='Enter the name of the section')
    parent=models.ForeignKey('self',blank=True,null=True)
    url=models.CharField(max_length=50,help_text='Enter Section Url')

    def __unicode__(self):
        return self.name
    
class Banner(models.Model):
    name=models.CharField(max_length=20,help_text='Helpful name to remember top banner')
    image=models.ImageField(upload_to=settings.MEDIA_ROOT + 'banner/')
    hide=models.BooleanField(blank=True,help_text='Hides Current Banner')
    
    def __unicode__(self):
        return self.name
    
    def save(self):
       super(Banner,self).save()
       fn='%s' %(settings.MEDIA_ROOT + self.image.name)
       width,height = [int(x) for x in settings.BANNER_DIMENSIONS.split('x')]
       imin=Image.open(fn)
       imout=imin.resize((width,height),Image.ANTIALIAS)
       imout.save(fn)