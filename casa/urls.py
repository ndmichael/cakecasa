from django.urls import path
from casa import views as shop_views

app_name = 'casa'

urlpatterns = [
    # path('category/', shop_views.product_list, name='product_list'),
    # path('<slug:category_slug>/', shop_views.product_list, name='product_list_by_category'),
    # path('<int:id>/<slug:slug>/', shop_views.product_detail, name='product_detail'),   
    path('', shop_views.index, name='casa-home'),
    path('about/', shop_views.about, name='casa-about'),
    path('contact_us/', shop_views.contact_view, name='casa-contact'),

]