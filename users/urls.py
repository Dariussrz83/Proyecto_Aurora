from django.urls import path
from users.views import login_view,register,update_user
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('signup/', register),
    path('update/', update_user),
]
