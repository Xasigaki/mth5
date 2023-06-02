from django.conf.urls.static import static
from shop_api import settings
from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', views.category_api_view),
    path('api/v1/categories/<int:id>/', views.category_detail_api_view),
    path('api/v1/products/', views.products_api_view),
    path('api/v1/products/<int:id>/', views.product_detail_api_view),
    path('api/v1/reviews/', views.reviews_api_view),
    path('api/v1/reviews/<int:id>/', views.review_detail_api_view),
    path('api/v1/products/reviews/', views.products_reviews_api_view),
    path('api/users/', include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)