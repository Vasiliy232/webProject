from django.db.models import Sum, Case, When, F, PositiveIntegerField, Prefetch
from rest_framework import mixins, viewsets
from .models import (
    Map,
    Structure,
    SubStructure,
    StructureUnit,
    Register,
    DataType
)
from .serializers import (
    MapSerializer,
    StructureSerializer,
    SubStructureSerializer,
    StructureUnitSerializer,
    RegisterSerializer,
    DataTypeSerializer
)
from .pagination import StructurePagination, RegisterPagination, SubStructurePagination


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
    queryset = Structure.objects.all().prefetch_related('registers').order_by('-id')
    serializer_class = StructureSerializer
    pagination_class = StructurePagination

    def get_queryset(self):
        return super().get_queryset().annotate(
            input_registers_number=Sum(
                Case(
                    When(registers__level='I', then=F('registers__data_type__bytes') / 2),
                    default=0,
                    output_field=PositiveIntegerField()
                )
            ),
            holding_registers_number=Sum(
                Case(
                    When(registers__level='H', then=F('registers__data_type__bytes') / 2),
                    default=0,
                    output_field=PositiveIntegerField()
                )
            )
        )

    def paginate_queryset(self, queryset):
        if self.request.query_params.get('no_pagination') == 'true':
            self.pagination_class = None
        return super().paginate_queryset(queryset)


class SubStructureMixinViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = SubStructure.objects.all().prefetch_related('structure__registers').order_by('-id')
    serializer_class = SubStructureSerializer
    pagination_class = SubStructurePagination


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
    queryset = Register.objects.all().select_related('data_type').order_by('-id')
    serializer_class = RegisterSerializer
    pagination_class = RegisterPagination

    def paginate_queryset(self, queryset):
        if self.request.query_params.get('no_pagination') == 'true':
            self.pagination_class = None
        return super().paginate_queryset(queryset)


class DatatTypeMixinViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer
