from django.urls import path
from .views import home, category_filter, product_detail 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('category/<str:category>/', category_filter, name='category_filter'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
