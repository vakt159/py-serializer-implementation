from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(required=True, max_length=64)
    model = serializers.CharField(required=True, max_length=64)
    horse_powers = serializers.IntegerField(required=True, validators=[
        MaxValueValidator(1914),
        MinValueValidator(1)])
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(required=False,
                                                allow_null=True,
                                                allow_blank=True)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get("manufacturer",
                                                   instance.manufacturer)
        instance.model = validated_data.get("model", instance.model)
        instance.horse_powers = validated_data.get("horse_powers",
                                                   instance.horse_powers)
        instance.is_broken = validated_data.get("is_broken",
                                                instance.is_broken)
        instance.problem_description = validated_data.get(
            "problem_description",
            instance.problem_description)

        instance.save()
        return instance
