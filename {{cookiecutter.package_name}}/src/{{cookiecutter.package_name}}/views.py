from django.views.generic.detail import DetailView

from . models import Product


class ProductDetailView(DetailView):
    model = Product
