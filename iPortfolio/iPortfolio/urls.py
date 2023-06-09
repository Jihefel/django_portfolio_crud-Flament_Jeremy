"""
URL configuration for azz project.

The  list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio-details/<int:id>', views.portfolio_details, name='portfolio-details'),
    path('admin/', views.index_admin, name='admin'),
    path('admin/edit/<str:section>', views.edit, name='edit'),
    path('admin/edit/<str:section>/<int:id>', views.edit, name='edit_details'),
    path('admin/delete/<str:section>/<str:property>', views.delete, name='delete')
]
