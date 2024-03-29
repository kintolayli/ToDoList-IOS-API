from rest_framework import routers
from rest_framework import permissions

from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from todo.views import TodoViewSet, UserViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="Документация API приложения ToDoApp-IOS",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="golkiper-leo@yandex.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', 
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
       name='schema-redoc'),
] 