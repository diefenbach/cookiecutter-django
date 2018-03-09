import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from {{cookiecutter.package_name}}.models import Product


@pytest.fixture
def product():
    return Product.objects.create(name='Hose')


@pytest.fixture
def browser(request):
    def finalizer():
        driver.close()
    request.addfinalizer(finalizer)

    driver = webdriver.Chrome()
    return driver


@pytest.mark.django_db()
def test_product(product):
    assert product.name == 'Hose'
