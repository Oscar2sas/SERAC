from django.urls import path
from UsuarioSession.views import * 

urlpatterns = [
    path('', login, name='Login'),
    path('registrar/', registrarUsuario),
    path('home/', home),
    path('logout/', logout),
]