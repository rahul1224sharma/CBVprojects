from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
class HelloWorldApp(View):
    def get(self,request):
        ss='''<h1>Hello from Class Based View </h1>
        <hr/>
        <h2>Response given for get method from client</h2>
        <h3>Have a nice day</h3>
        '''
        return HttpResponse(ss)

from django.views.generic import TemplateView
class Template(TemplateView):
    template_name = 'MyApps1/home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='rahul'
        context['age']=26
        context['height']=5.8
        return context

from MyApps1.models import Book
from django.views.generic import ListView
class BookListview(ListView):
    model=Book;


from MyApps1.models import Company
from django.views.generic import ListView,DetailView

class CompanyListView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company
