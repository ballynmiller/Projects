from django.db import models
from django.conf import settings

from PIL import Image

LOCATION_CHOICES=(
   ('top right', 'top right'), 
   ('bottom right', 'bottom right'),
)

SIZES=(
  ('310x170','Width: 310 by Height:170'),
)

class Ad(models.Model):
    location=models.CharField(max_length=200,choices=LOCATION_CHOICES)
    size=models.CharField(max_length=20,choices=SIZES)
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to=settings.MEDIA_ROOT + 'ads/')
    
    def __unicode__(self):
        return self.name
    
    def save(self):
       super(Ad,self).save()
       fn='%s' %(settings.MEDIA_ROOT + self.image.name)
       width,height = [int(x) for x in self.size.split('x')]
       imin=Image.open(fn)
       imout=imin.resize((width,height),Image.ANTIALIAS)
       imout.save(fn)
