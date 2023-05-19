from django.urls import path
from guestbook.views import *

urlpatterns = [
    # TEST
    path('', hello_world, name = 'hello_world'),

    path('create/', create_guestbook, name='create_guestbook'),
    path('list/', list_guestbook, name='list_guestbook'),
    path('delete/<int:id>/', delete_guestbook, name='delete_guestbook'),
]