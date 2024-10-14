from django.urls import path
from home.views import (
    get_chocolates,
    create_chocolate,
    update_chocolate,
    partial_update_chocolate,
    delete_chocolate,
)

urlpatterns = [
    path('chocolates/', get_chocolates, name='get_chocolates'),
    path('chocolates/create/', create_chocolate, name='create_chocolate'),
    path('chocolates/update/<int:id>/', update_chocolate, name='update_chocolate'),
    path('chocolates/partial_update/<int:id>/', partial_update_chocolate, name='partial_update_chocolate'),
    path('chocolates/delete/<int:id>/', delete_chocolate, name='delete_chocolate'),
]
