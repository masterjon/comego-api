from django.conf.urls import url, include
from api import views
# from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'actividades_simple', views.CategoryItemViewSet)
router.register(r'actividades', views.CategoryNestedItemViewSet)
router.register(r'boletines', views.BoletinViewSet)
router.register(r'guias', views.GuiaViewSet)
router.register(r'podcast', views.PodcastViewSet)
router.register(r'leyes', views.LeyViewSet)
router.register(r'normas', views.NormaViewSet)
router.register(r'reglamentos', views.ReglamentoViewSet)
# router.register(r'categories', views.AnimalCategoryViewSet, base_name='categories')
# router.register(r'markers-categories', views.CategoryMarkerViewSet, base_name='categories_markers')

# category_router = routers.NestedSimpleRouter(router, r'categories', lookup='category')

# category_router.register(r'animal', views.AnimalViewSet, base_name='animal_detail')

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    # url(r'^', include(category_router.urls)),
    # url(r'^related-animals/$', views.RelatedAnimalsView.as_view(), name='related_animals'),
]
