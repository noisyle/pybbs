#-*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage
from bbs.models import Thread

# Create your views here.
def index(request,page=1):
    paginator = Paginator(Thread.objects.order_by("-pub_date"), 10)
    try:
        thread_list = paginator.page(page)
    except EmptyPage:
        return HttpResponseRedirect(reverse('bbs:index', args=(paginator.num_pages,)))

    return render(request,"bbs/index.html",{"thread_list":thread_list})

def post_thread(request):
    thread = Thread(title=request.POST['title'], content=request.POST['content'])
    thread.save()
    return HttpResponseRedirect(reverse('bbs:index'))

def thread(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    comments = thread.comment_set.order_by("-pub_date")
    return render(request,"bbs/thread.html",{"thread":thread,"comments":comments})

def send_comment(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    thread.comment_set.create(content=request.POST['content'])
    return HttpResponseRedirect(reverse('bbs:thread', args=(thread.id,)))
