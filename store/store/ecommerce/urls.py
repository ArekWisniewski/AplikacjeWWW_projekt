from django.urls import path
from . import views

urlpatterns = [
    path('categories/create', views.category_create),
    path('categories', views.category_list),
    path('categories/<int:pk>', views.category_detail),
    path('categories/<int:pk>/update', views.category_update),
    path('categories/<int:pk>/delete', views.category_delete),

    path('customers/create', views.customer_create),
    path('customers/<int:pk>', views.customer_detail),
    path('customers/<int:pk>/update', views.customer_update),
    path('customers/<int:pk>/delete', views.customer_delete),

    path('products/create', views.products_create),
    path('products/<query>', views.products_search),
    path('products/<int:pk>', views.products_detail),
    path('products/<int:pk>/update', views.products_update),
    path('products/<int:pk>/delete', views.products_delete),

    path('orders/create', views.order_update),
    path('orders', views.order_list),
    path('orders/<int:pk>', views.order_detail),
    path('orders/<int:pk>/update', views.order_update),
    path('orders/<int:pk>/delete', views.order_delete),
]
