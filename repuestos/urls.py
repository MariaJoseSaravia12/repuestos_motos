from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [    
    #path('accounts/', include('registration.backends.default.urls')),
    path('', include('vistaprevia.urls')),  
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('contacto/', include('contacto.urls')),
    path('tienda/', include('tienda.urls')),
    path('usuarios/', include('usuarios.urls')),    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
