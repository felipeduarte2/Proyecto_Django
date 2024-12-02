"""
URL configuration for myproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# ---------------------------------------
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('holaMundo/', views.hola_mundo, name='hola_mundo'),
    path('', views.principal, name='principal'),
    path('bienvenido/<str:nombre>/<str:lugar>/', views.bienvenido,name='bienvenido'),
    path('bienvenido/', views.bienvenido,name='bienvenido'),
    path('bienvenido/<str:nombre>/', views.bienvenido,name='bienvenido'),
    path('bienvenido/<str:nombre>/<str:lugar>/', views.bienvenido,name='bienvenido'),
    path('web/', views.web,name='web'),
    path('python/', views.python,name='python'),
    path('borrar-sw/<int:id>',views.borrar_software, name='borrar_software'),
    path('guardar-sw-get/',views.guardar_sw_get,name='guardar_sw_get'),
    path('guardar-sw-post/',views.guardar_sw_post,name='guardar_sw_post'),
]