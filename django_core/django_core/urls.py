from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from storage.sites import filebrowser_site


urlpatterns = [
    path("admin/filebrowser/", filebrowser_site.urls),
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("storage/", include("storage.urls")),
    # API patterns
    path("api/subscriptions/", include("subscriptions.urls")),
    path("api/marketplaces/", include("marketplaces.urls")),
    path("api/news/", include("news.urls")),
    path("api/contacts/", include("contacts.urls")),
    path("api/registration/", include("registration_on_event.urls")),
    path("api/info/", include("info.urls")),
    path("api/laboratories/", include("laboratories.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
