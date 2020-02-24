from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Elog
from .forms import ElogFrom


def elog_detail(request, log_id):
    obj = get_object_or_404(Elog, id=log_id)
    # obj = Elog.objects.get(id=log_id)
    template_name = "elog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

def elog_list(request):
    qs = Elog.objects.all()
    template_name = "elog/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)

def elog_create(request):
    form = ElogFrom(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    template_name = "elog/create.html"
    context = {"form": form}
    return render(request, template_name, context)

def elog_update(request):
    template_name = "elog/update.html"
    context = {"object": 1}
    return render(request, template_name, context)
