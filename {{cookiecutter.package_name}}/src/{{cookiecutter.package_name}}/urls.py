from django.urls import path

from . views import ProductDetailView


app_name = '{{cookiecutter.package_name}}'
urlpatterns = [
    path('product/<int:pk>/detail/', ProductDetailView.as_view(), name='product-detail'),
]
