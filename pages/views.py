from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django import forms
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.exceptions import ValidationError



# Create your views here.
class homePageView(TemplateView):
    template_name='../templates/pages/home.html'
    
    
class AboutPageView(TemplateView):
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
    template_name = 'pages/contact.html'


class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price":"100.00"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":"200.00"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":"300.00"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":"400.00"},
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'


    def get(self, request, id):
        try:
            product = Product.products[int(id) - 1]  # Attempt to access the product
        except (IndexError, ValueError):  # Handle invalid product numbers
            return redirect('home')  # Redirect to the home page
        viewData = {}
        product = Product.products[int(id)-1]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] =  product["name"] + " - Product information"
        viewData["price"] = str(product["price"]) + " - Product Price"
        viewData["product"] = product

        return render(request, self.template_name, viewData)
class ProductForm(forms.Form): 

    name = forms.CharField(required=True) 

    price = forms.FloatField(required=True)
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return price

 

 

class ProductCreateView(View):

    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {"title": "Create product", "form": form}
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Add product creation logic here (save data to database, etc.)
            # For demonstration purposes, we'll simulate product creation:
            new_product = {
                "id": str(len(Product.products) + 1),  # Assuming you have product data storage
                "name": form.cleaned_data["name"],
                "price": form.cleaned_data["price"],
            }
            Product.products.append(new_product)
            return HttpResponseRedirect('/products/create/success/')  # Redirect to new template
        else:
            viewData = {"title": "Create product", "form": form}
            return render(request, self.template_name, viewData)
        
        
class CreatedPageView(TemplateView):
    template_name = 'products/created.html'

