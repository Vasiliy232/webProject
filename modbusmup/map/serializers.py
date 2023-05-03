from rest_framework import serializers
from .models import Map, Structure, SubStructure, StructureUnit, Register, DataType
from django.contrib.auth.models import User


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'


class StructureSerializer(serializers.ModelSerializer):
    input_registers_number = serializers.ReadOnlyField()
    holding_registers_number = serializers.ReadOnlyField()

    class Meta:
        model = Structure
        fields = ['id', 'name', 'registers', 'input_registers_number', 'holding_registers_number']


class SubStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubStructure
        fields = '__all__'


class StructureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StructureUnit
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли должны совпадать'})
        user.set_password(password)
        user.save()
        return user
