#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.http import HttpResponse
import datetime  # datetime

# create  a hello view


def hello(request):
    return HttpResponse("Hello World")

# create a active view


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours.it will be %s.</body></html>" % (
        offset, dt)
    return HttpResponse(html)