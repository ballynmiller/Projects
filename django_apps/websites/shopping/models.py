from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from websites.content.models import Section
from websites.contact.models import Contact

from PIL import Image

class Size(models.Model):
    name=models.CharField(max_length=10,help_text='Example xxl... or small...')
    
    def __unicode__(self):
        return self.name
    
class Item(models.Model):
    name=models.CharField(max_length=150,help_text='Name of the item')
    price=models.CharField(max_length=999)
    section=models.ManyToManyField(Section)
    sizes=models.ManyToManyField(Size)
    desc=models.TextField(verbose_name="Description")
    oos=models.BooleanField(default=False,blank=True,verbose_name="Is The Item Out of Stock?")
    
    def __unicode__(self):
        return self.name
    
    def get_media(self):
        return Media.objects.filter(item=self)

    def get_first_image(self):
        try:
            return Media.objects.filter(item=self)[:1].get()
        except ObjectDoesNotExist: 
            pass

class Media(models.Model):
    class Meta: 
        verbose_name_plural = 'Media'
    item=models.ForeignKey(Item)
    image=models.ImageField(upload_to=settings.MEDIA_ROOT + 'media/')
    name=models.CharField(max_length=20,help_text='Something to help remember the images')
    
    def __unicode__(self):
        return self.name
    
    def save(self):
       super(Media,self).save()
       fn='%s' %(self.image.name)
       width,height = [int(x) for x in "500x500".split("x")]
       imin=Image.open(fn)
       imout=imin.resize((width,height),Image.ANTIALIAS)
       imout.save(fn)

class Group(models.Model):
    name=models.CharField(max_length=20,)
    items=models.ManyToManyField(Item)
    discount=models.CharField(max_length=999)
    
    def __unicode__(self):
        return self.name
