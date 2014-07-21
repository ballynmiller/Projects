from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from websites.shopping.models import Item, Media
from websites.content.models import Section
from urllib import urlencode

import urllib2


def section(request, section_url):
    s = all_subsecs = None
    item_list = []
    try:
        s = Section.objects.get(url=section_url)
    except ObjectDoesNotExist:
        raise Http404

    all_subsecs = s.section_set.all()
    if all_subsecs:
        for a in all_subsecs:
            items = a.item_set.all()
            item_list.append(items)
    else:
        item_list = s.item_set.all()
    return render_to_response("item_list.html", {
        'item_list': item_list,
        'section': s
    }, RequestContext(request), )


def detail(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        raise Http404

    try:
        image = Media.objects.filter(item=item)[:1].get()
    except ObjectDoesNotExist:
        image = None

    return render_to_response('detail.html', {'item': item, 'large_image': image, }, RequestContext(request), )