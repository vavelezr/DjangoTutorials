""" Module contains views for pages. """
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError
from .models import Product


# Create your views here.
class HomePageView(TemplateView):
    """ Class represents the Home page. """
    template_name='../templates/pages/home.html'
class AboutPageView(TemplateView):
    """ Class represents the About page. """
    template_name = 'pages/about.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "Contact: 3040000",
            "author": "Developed by: Vaneeee",
            "email": "e-mail: mibebitofiufiu@gmail.com",
            "address": "Address: Cuenca, España",
            "phone": "Phone: 302302302",
        })

        return context
class ContactPageView(TemplateView):
    """ Class represents the Contact page. """
    template_name = 'pages/contact.html'


class ProductIndexView(View):
    """Class represents the Product Index page. """
    template_name = 'products/index.html'
    
    def get(self, request):
        """ Function returns the Product Index page. """
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.objects.all()

        return render(request, self.template_name, viewData)

class ProductShowView(View): 
    """ Class represents the Product Show page. """

    template_name = 'products/show.html' 
    def get(self, request, id): 
        """ Function returns the Product Show page. """
        # Check if product id is valid 
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError("Product id must be 1 or greater")
            product = get_object_or_404(Product, pk=product_id)
        except (ValueError, IndexError): 
            # If the product id is not valid, redirect to the home page
            return HttpResponseRedirect(reverse('home'))

        viewData = {}
        product = get_object_or_404(Product, pk=product_id)
        viewData["title"] = product.name + " - Online Store"
        viewData["subtitle"] =  product.name + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)



class ProductListView(ListView): 
    """ Class represents the Product List page. """

    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'  # This will allow you to loop through 'products'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Products - Online Store' 
        context['subtitle'] = 'List of products' 
        return context 
    
class ProductForm(forms.ModelForm):
    """ Class represents the Product form. """

    
    class Meta:
        model = Product
        fields = ['name', 'price']
        
    def clean_price(self):
        """ Function checks if price is greater than zero. """
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return price





class ProductCreateView(View):

    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/create/success/')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            
            return render(request, self.template_name, viewData) 


class CreatedPageView(TemplateView):
    template_name = 'products/created.html'

