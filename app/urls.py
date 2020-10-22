from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'anumarrage'

urlpatterns = [
    path('anusha-weds-chethan/',views.home,name='home'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)