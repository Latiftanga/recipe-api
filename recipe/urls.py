from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()  # Creates routes for all methods supported by the viewset.
router.register('tags', views.TagViewSets)
router.register('ingredients', views.IngredientViewSetAPIView)
router.register('recipes', views.RecipeViewSetAPIView)

app_name = 'recipe'


urlpatterns = [
    path('', include(router.urls))
]
