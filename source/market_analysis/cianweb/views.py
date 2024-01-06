from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .utils import DataMixin
from .forms import *
import logging

class HomeView(DataMixin, View):
    template_name = 'cianweb/home.html'

    def get_context_data(self):
        context = self.get_user_context(title='About application')
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
class ParserView(DataMixin, View):
    template_name = 'cianweb/parser.html'
    form_class=ParsingForm

    def get_context_data(self):
        context = self.get_user_context(title='Collecting information', form=self.form_class)
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = ParsingForm(request.POST)
        if form.is_valid():
            return render(request, self.template_name, self.get_context_data(**kwargs))
            # try to parse cian
        else:
            return render(request, self.template_name, self.get_context_data(**kwargs))
    
class VisualizeView(DataMixin, View):
    template_name = 'cianweb/visualize.html'

    def get_context_data(self):
        context = self.get_user_context(title='Visualization data')
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

class TrainView(DataMixin, View):
    template_name = 'cianweb/train.html'

    def get_context_data(self, **kwargs):
        context = self.get_user_context(title='Training ML models')
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
def getMetro(request):
    city = request.GET.get('city')
    metro = Metro.objects.filter(city=city).order_by('name').values('id', 'name')
    if len(metro) == 0:
        metro = [{'id': -1, 'name': 'Нет станций метро'}]
    else:
        metro = [{'id': 0, 'name': 'Все станции метро'}] + list(metro)
    return JsonResponse(metro, safe=False)