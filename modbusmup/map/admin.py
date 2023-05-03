from django.contrib import admin
from .models import (
    Map,
    Structure,
    SubStructure,
    StructureUnit,
    Register,
    DataType
)

admin.site.register(Map)
admin.site.register(SubStructure)
admin.site.register(StructureUnit)
admin.site.register(Register)
admin.site.register(DataType)


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ["name"]
