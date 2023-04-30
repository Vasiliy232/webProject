from rest_framework import mixins, viewsets
from .models import Map, Structure, SubStructure, StructureUnit, Register, DataType
from .serializers import MapSerializer, StructureSerializer, SubStructureSerializer, StructureUnitSerializer, \
    RegisterSerializer, DataTypeSerializer
from .pagination import StructurePagination, RegisterPagination


class MapMixinViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class StructureMixinViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Structure.objects.all().prefetch_related('registers')
    serializer_class = StructureSerializer
    pagination_class = StructurePagination


class SubStructureMixinViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = SubStructure.objects.all()
    serializer_class = SubStructureSerializer


class StructureUnitMixinViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = StructureUnit.objects.all()
    serializer_class = StructureUnitSerializer


class RegisterMixinViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    pagination_class = RegisterPagination


class DatatTypeMixinViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer
