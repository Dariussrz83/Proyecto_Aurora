from django.urls import path

from cakes.views import create_cake, list_cakes,list_birthday,create_birthday,list_alfajores,create_alfajores


urlpatterns=[
    path('create-cake/', create_cake),
    path('list-cakes/', list_cakes),
    path('list-birthday/', list_birthday ),
    path('create-birthday/', create_birthday),
    path('list-alfajores/', list_alfajores),
    path('create-alfajores/', create_alfajores),
    
]