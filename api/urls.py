from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating the routers
router = DefaultRouter(schema_title='Pastebin API')
router.register(r'belstops', views.BelStopViewSet)
router.register(r'belmeetings', views.BelMeetingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
