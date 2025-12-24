import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)

    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    validated_data = serializer.validated_data

    return Car.objects.create(
        manufacturer=validated_data["manufacturer"],
        model=validated_data["model"],
        horse_powers=validated_data["horse_powers"],
        is_broken=validated_data["is_broken"],
        problem_description=validated_data.get("problem_description"),
    )
