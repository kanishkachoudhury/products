from django.urls import path
from product import views

urlpatterns = [
    path('createcatagory', views.create_catagory, name='createcatagory'),
    path('catagory/<int:category_id>/update', views.update_catagory, name='updatecatagory'),
    path('catagory/<int:category_id>/delete', views.delete_catagory, name='deletecatagory'),
    path('getcatagory', views.get_all_catagory,name='getcatagory'),
    path('createproduct', views.create_catagory, name='createproduct'),
    path('updateproduct', views.update_product, name='updateproduct'),
    path('deleteproduct', views.delete_product, name='deleteproduct'),
    path('getproduct', views.get_all_product,name='getproduct'),
    path('getproductbytitle', views.get_product_by_name, name='getproductbytitle')
]