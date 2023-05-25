from django.db import models


class Map(models.Model):
    name = models.CharField(max_length=30, blank=False)
    sub_structure = models.ManyToManyField('SubStructure')

    def __str__(self):
        return f'{self.name}'


class Structure(models.Model):
    name = models.CharField(max_length=30, blank=False)
    registers = models.ManyToManyField('Register')

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

    def __str__(self):
        return f'{self.name}'
