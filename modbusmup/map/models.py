from django.db import models
from django.contrib.auth.models import AbstractUser


class Map(models.Model):
    name = models.CharField(max_length=30, blank=False)
    sub_structure = models.ManyToManyField('SubStructure')

    def __str__(self):
        return f'{self.name}'


class Structure(models.Model):
    name = models.CharField(max_length=30, blank=False)
    input_registers_number = models.PositiveIntegerField(default=0)
    holding_registers_number = models.PositiveIntegerField(default=0)
    registers = models.ManyToManyField('Register')

    def get_input_registers_count(self):
        registers = Register.objects.filter(structure=self, level='I').prefetch_related('structure')
        self.input_registers = registers.count()
        return self.input_registers

    get_input_registers_count.short_description = "number of input registers"

    def get_holding_registers_count(self):
        registers = Register.objects.filter(structure=self, level='H').prefetch_related('structure')
        self.holding_registers = registers.count()
        return self.holding_registers

    get_holding_registers_count.short_description = "number of holding registers"

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


class SubStructure(models.Model):
    name = models.CharField(max_length=30, default='-')
    description = models.TextField(blank=True)
    structure = models.ForeignKey('Structure', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class StructureUnit(models.Model):
    name = models.CharField(max_length=30, blank=False)
    sub_structure = models.ManyToManyField('SubStructure')
    map = models.ForeignKey('Map', null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class DataType(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    name = models.CharField(max_length=10, blank=False)
    bytes = models.PositiveIntegerField(default=2)

    def __str__(self):
        return f'{self.name}'


class Register(models.Model):
    INPUT = "I"
    HOLDING = "H"

    LEVEL_CHOICES = [
        (INPUT, "input"),
        (HOLDING, "holding")
    ]

    name = models.CharField(max_length=30, blank=False)
    data_type = models.ForeignKey('DataType', null=True, default=None, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
