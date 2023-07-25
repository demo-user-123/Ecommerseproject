from . import views
from django.urls import path

app_name = 'shopapp'

urlpatterns = [
    path('', views.allProdCat, name='all_products'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:pro_slug>/', views.proDetail, name='product_category_details'),

]
