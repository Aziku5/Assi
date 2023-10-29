from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic



#список фильмов (неполная информация)
class CartoonListView(generic.ListView):
    template_name = 'cartoons/cartoons_list.html'
    queryset = models.Disney.objects.all()

    def get_queryset(self):
        return models.Disney.objects.all()




# def cartoonView(request):
#     cartoon_value = models.Disney.objects.all()
#     html_name = 'cartoons/cartoons_list.html'
#     context = {
#         'cartoon_key': cartoon_value,
#     }
#     return render(request, html_name, context)


#детальная информация

class CartoonDetailView(generic.DetailView):
    template_name = 'cartoons/cartoon_detail.html'

    def get_object(self, **kwargs):
        cartoon_id = self.kwargs.get('id')
        return get_object_or_404(models.Disney, id=cartoon_id)


# def cartoonDetailView(reques, id):
#     cartoon_id = get_object_or_404(models.Disney, id=id)
#     html_name = 'cartoons/cartoon_detail.html'
#     context = {
#         'cartoon_id': cartoon_id,
#     }
#     return render(reques, html_name, context)


# create

class CreateCartoonView(generic.CreateView):
    template_name = 'cartoons/create_cartoon.html'
    form_class = forms.DisneyForm
    queryset = models.Disney.objects.all()
    success_url = '/all_cartoons/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCartoonView, self).form_valid(form=form)


# def creatCartoonView(request):
#     method = request.method
#     if method == "POST":
#         form = forms.DisneyForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Мультфильм успешно добавлен')
#     else:
#         form = forms.DisneyForm()
#
#     return render(request, 'cartoons/create_cartoon.html', {'form': form})


# delete
class DeleteCartoonView(generic.DeleteView):
    template_name = 'cartoons/confirm_delete.html'
    success_url = '/all_cartoons/'

    def get_object(self, **kwargs):
        cartoon_id = self.kwargs.get('id')
        return get_object_or_404(models.Disney, id=cartoon_id)

# def deleteCartoonView(request, id):
#     cartoon_id = get_object_or_404(models.Disney, id=id)
#     cartoon_id.delete()
#     return HttpResponse('Мультфильм успешно удален')


# update
class UpdateCartoonView(generic.UpdateView):
    template_name = 'cartoons/update_cartoons.html'
    form_class = forms.DisneyForm
    success_url = '/all_cartoons/'

    def get_object(self, **kwargs):
        cartoon_id = self.kwargs.get('id')
        return get_object_or_404(models.Disney, id=cartoon_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateCartoonView, self).form_valid(form=form)

# def updateCartoonView(request, id):
#     cartoon_id = get_object_or_404(models.Disney, id=id)
#     if request.method == 'POST':
#         form = forms.DisneyForm(instance=cartoon_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Мультфильм успешно изменен')
#
#     else:
#         form = forms.DisneyForm(instance=cartoon_id)
#     return render(request, 'cartoons/update_cartoons.html',
#                   {
#                       'form': form,
#                       'cartoon_id': cartoon_id
#                   }
#                   )


class Search(generic.ListView):
    template_name = 'cartoons/cartoons_list.html'
    context_object_name = 'cartoon'
    paginate_by = 5

    def get_queryset(self):
        return models.Disney.objects.filter(title__icontains=self.request.GET.get('q'))


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
