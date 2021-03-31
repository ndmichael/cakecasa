from django.urls import path
from casa import views as shop_views

app_name = 'casa'

urlpatterns = [
    path('', shop_views.index, name='casa-home'),
    path('about/', shop_views.about, name='casa-about'),
    path('contact_us/', shop_views.contact_view, name='casa-contact'),
    path('cakes/', shop_views.contact_view, name='casa-cakes'),
    path('milkshakes/', shop_views.milkshakes, name='milkshakes'),
    path('cakecategory/', shop_views.cake_list, name='cake_list'),
    path('<slug:category_slug>/', shop_views.cake_list, name='cake_list_by_category'),
    path('<int:id>/<slug:slug>/', shop_views.cake_detail, name='cake_detail'),
    # path('<int:id>/<slug:slug>/', shop_views.product_detail, name='product_detail'),   
    
]