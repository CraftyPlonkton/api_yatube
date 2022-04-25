from django.urls import path, include

from rest_framework import routers

from api.views import GroupViewSet, PostViewSet, CommentViewSet, FollowView

router_v1 = routers.DefaultRouter()
router_v1.register(r'groups', GroupViewSet)
router_v1.register(r'posts', PostViewSet)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path(r'v1/', include('djoser.urls')),
    path(r'v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
    path('v1/follow/', FollowView.as_view()),
]
