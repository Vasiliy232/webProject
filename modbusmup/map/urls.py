from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets
from . import views

app_name = 'map'

router = DefaultRouter()
router.register(r'map', viewsets.MapMixinViewSet)
router.register(r'structure', viewsets.StructureMixinViewSet)
router.register(r'substructure', viewsets.SubStructureMixinViewSet)
router.register(r'unit', viewsets.StructureUnitMixinViewSet)
router.register(r'register', viewsets.RegisterMixinViewSet)
router.register(r'data_type', viewsets.DatatTypeMixinViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/register/', views.UserRegistrationApiView.as_view(), name='user_registration')
]
