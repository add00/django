# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views import generic

from news.models import *
from news import models

def index(request):
	news = News.objects.all().order_by('-id')
	return render_to_response('index.html',
			{'news': news },
			context_instance=RequestContext(request))

class NewsList(generic.ListView):
    model = models.News
    paginate_by = 1
    context_object_name = 'news_list'

news_list = NewsList.as_view()