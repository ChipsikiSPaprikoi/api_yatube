from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
    path('v1/', include(router.urls)),
]
