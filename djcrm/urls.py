
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from leads import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingView.as_view(), name="home"),
    path('leads/', include('leads.urls')),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', views.CustomLogoutView.as_view(), name="logout"),
    path('signup/', views.SignUpView.as_view(), name="signup")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
