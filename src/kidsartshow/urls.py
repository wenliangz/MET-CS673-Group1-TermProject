"""kidsartshow URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from arts.views import ArtListView as MainView
from accounts.views import login_view,logout_view,register_view,UserDashboard

urlpatterns = [
    #re_path('^$', MainView.as_view(), name = 'homepage'),
    path('', TemplateView.as_view(template_name = 'home.html'), name='home'),
    path('accounts/', UserDashboard.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),
    path('arts/', include('arts.urls')),
    path('login/', login_view, name ='login'),
    path('logout/', logout_view, name ='logout'),
    path('register/', register_view, name ='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)