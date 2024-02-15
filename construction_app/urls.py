from django.urls import path
from .views import ListProductView, CreateProductView, UpdateDeleteView
from .views import send_email

urlpatterns=[
    path('list_product/', ListProductView.as_view(), name='list-product'),
    path('create_product/', CreateProductView.as_view(), name='create-product'),
    path('update_delete_product/<str:pk>/', UpdateDeleteView.as_view(), name='update-delete-product' ),
    path('send-email/', send_email, name='send-mail'),
]
