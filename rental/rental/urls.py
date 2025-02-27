from django.contrib import admin
from django.urls import path, include
from listings.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts.views import user_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', user_login, name='login'),

    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('accounts.urls')),
    path('listings/', include('listings.urls')),
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
