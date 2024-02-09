from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import index_view, contact_view, about_view, blog_view, blog_single_view

urlpatterns = [
    path('', index_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('articles/', blog_view),
    path('blog/<int:pk>/', blog_single_view, name='blog-single')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
