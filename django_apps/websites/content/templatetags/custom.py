from django import template 
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.template import Variable

from websites.content.models import Section,Banner
from websites.contact.models import Contact
from websites.shopping.models import Item, Group
from websites.ads.models import Ad

register = template.Library()

@register.tag
def get_sections(parser,token):
    return SectionNode()

class SectionNode(template.Node):
    def __init__(self):
        pass 
    def render(self,context):
        sections=Section.objects.all()
        context['section_list']=sections
        return ''

   
@register.tag 
def get_banner(parser,token):
    return BannerNode()

class BannerNode(template.Node):
    def __init__(self):
        pass
    def render(self,context):
        try:
            banner=Banner.objects.filter(hide=False)[:1].get()
        except ObjectDoesNotExist:
            return ''
        context['banner']=banner
        return ''

class SettingsNode(template.Node):
    def __init__(self,prop): 
        self.prop = prop 
    def render(self,context):
        return self.prop
    
@register.tag    
def get_media_url(parser,token):
    return SettingsNode(settings.MEDIA_URL)

class TopRightNode(template.Node):
    def render(self, context):
        try: 
            context['top_right']= Ad.objects.filter(location='top right')[:1].get()
        except ObjectDoesNotExist: 
            return ''
        return ''

@register.tag
def get_top_right(parser,token):
    return TopRightNode()

class BottomRightNode(template.Node):
    def render(self, context):
        try: 
            context['bottom_right'] = Ad.objects.filter(location='bottom right')[:1].get()
        except ObjectDoesNotExist: 
            return ''
        return ''
    
@register.tag
def get_bottom_right(parser,token):
    return BottomRightNode()

class ContactNode(template.Node):
    def __init__(self,user):
        self.user = Variable(user)
    def render(self,context):
        try:
            contact = Contact.objects.filter(user=self.user.resolve(context)).get()
        except ObjectDoesNotExist:
            contact=None 
        context['contact']=contact
        return ''

@register.tag
def get_contact(parser,token):
    tag_name, user = token.contents.split()
    return ContactNode(user)

class DiscountNode(template.Node):
    def __init__(self,item):
        self.item = Variable(item)
    def render(self,context):
        item = self.item.resolve(context)
        price = item.price
        if not item: 
            return ''
        try: 
            group = Group.objects.filter(items=item)
        except ObjectDoesNotExist: 
            group = None
        if group: 
            price = float(item.price) - float(group[0].discount)
        context['price']= price
        return ''

@register.tag
def get_price(parser,token):
    tag_name, item = token.contents.split()
    return DiscountNode(item)