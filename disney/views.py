from django.shortcuts import render, get_object_or_404
from . import models


def cartoonView(request):
    cartoon_value = models.Disney.objects.all()
    html_name = 'cartoons/cartoons_list.html'
    context = {
        'cartoon_key': cartoon_value,
    }
    return render(request, html_name, context)



def cartoonDetailView(reques, id):
    cartoon_id = get_object_or_404(models.Disney, id=id)
    html_name = 'cartoons/cartoon_detail.html'
    context = {
        'cartoon_id': cartoon_id,
    }
    return render(reques, html_name, context)