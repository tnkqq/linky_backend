

from django.urls import include, path
from rest_framework.routers import SimpleRouter


from .views import (ResourceViewSet, TagViewSet, CategoryViewSet, GroupViewSet)



app_name = 'api'

router_v1 = SimpleRouter()


router_v1.register('resources', ResourceViewSet, basename='resources')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register('tags', TagViewSet, basename='tags')
router_v1.register('category', TagViewSet, basename='category')


urlpatterns = [
    path(
        'v1/', include(
            [path("", include("djoser.urls.jwt")),
                path('', include(router_v1.urls))
            ]
        )
    )
]

