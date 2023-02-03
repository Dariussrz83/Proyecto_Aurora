from django.urls import path

from cakes.views import create_cake, list_cakes,list_birthday,create_birthday,list_alfajores,create_alfajores, birthday_update,alfajores_update,cakes_update, Frozen_cakesDeleteView,Birthday_cakesDeleteView,AlfajoresDeleteView,about


urlpatterns=[
    path('create-cake/', create_cake),
    path('list-cakes/', list_cakes),
    path('list-birthday/', list_birthday ),
    path('create-birthday/', create_birthday),
    path('list-alfajores/', list_alfajores),
    path('create-alfajores/', create_alfajores),
    path('update-birthday/<int:pk>/', birthday_update),
    path('update-alfajores/<int:pk>/',alfajores_update),
    path('update-cakes/<int:pk>/',cakes_update),
    path('delete-cakes/<int:pk>/', Frozen_cakesDeleteView.as_view()),
    path('delete-birthday/<int:pk>/',Birthday_cakesDeleteView.as_view()),
    path('delete-alfajores/<int:pk>/',AlfajoresDeleteView.as_view()),
    path('about/',about),
]