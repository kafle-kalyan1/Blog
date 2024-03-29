from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def handler404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('admin/', include('admin_soft.urls')),
    path('', include("home.urls")),
    path('blog/', include("Blog.urls")),
    path('account/', include("Account.urls")),
]

handler404 = handler404

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
