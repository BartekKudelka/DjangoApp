from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('main/', include('main.urls')),
                  path('admin/', admin.site.urls),
                  path('login/', auth_views.LoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(),name='logout')
                  # path('new/', new_event, name='new_event')
                  # path('edit/', , edit_event, name='edit_event')
                  # path('delete/', delete_event, name='delete_event')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
