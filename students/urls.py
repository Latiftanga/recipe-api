from django.urls import path, include

from rest_framework.routers import DefaultRouter

from students import views

router = DefaultRouter()  # Creates routes for all methods supported by the viewset.
router.register('classes', views.ClassAPIViewSet)


app_name = 'students'


urlpatterns = [
    path('', include(router.urls))
]
