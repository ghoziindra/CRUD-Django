from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Home
    path('', views.home, name="home"),
    #Add Product
    path('add_product', views.add_product, name="add_product"), # type: ignore
    #View Product Individually
    path('product/<str:product_id>', views.product, name="product"), # type: ignore
    #Edit Product
    path('edit_product', views.edit_product, name="edit_product"), # type: ignore
    #Delete Product
    path('delete_product/<str:product_id>', views.delete_product, name="delete_product"),
]
