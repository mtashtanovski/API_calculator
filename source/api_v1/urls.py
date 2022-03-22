from django.urls import path

from api_v1.views import (
    echo_view,
    get_csrf_token,
    add,
    subtract,
    multiply,
    divide,
)

urlpatterns = [
    path('echo/', echo_view),
    path("get-csrf-token/", get_csrf_token),
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide')
]
