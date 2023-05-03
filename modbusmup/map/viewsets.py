from django.db.models import Sum, Case, When, F, PositiveIntegerField
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
    queryset = Register.objects.all().order_by('-id')
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
