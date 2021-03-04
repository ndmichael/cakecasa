from django.urls import path
from casa import views as shop_views

app_name = 'shop'

urlpatterns = [
    # path('category/', shop_views.product_list, name='product_list'),
    # path('<slug:category_slug>/', shop_views.product_list, name='product_list_by_category'),
    # path('<int:id>/<slug:slug>/', shop_views.product_detail, name='product_detail'),   
    path('', shop_views.index, name='casa-home'),

]