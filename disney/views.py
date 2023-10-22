from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms


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


# create
def creatCartoonView(request):
    method = request.method
    if method == "POST":
        form = forms.DisneyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Мультфильм успешно добавлен')
    else:
        form = forms.DisneyForm()

    return render(request, 'cartoons/create_cartoon.html', {'form': form})


# delete
def deleteCartoonView(request, id):
    cartoon_id = get_object_or_404(models.Disney, id=id)
    cartoon_id.delete()
    return HttpResponse('Мультфильм успешно удален')


# update
def updateCartoonView(request, id):
    cartoon_id = get_object_or_404(models.Disney, id=id)
    if request.method == 'POST':
        form = forms.DisneyForm(instance=cartoon_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Мультфильм успешно изменен')

    else:
        form = forms.DisneyForm(instance=cartoon_id)
    return render(request, 'cartoons/update_cartoons.html',
                  {
                      'form': form,
                      'cartoon_id': cartoon_id
                  }
                  )
