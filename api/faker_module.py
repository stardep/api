import json

from faker import Faker
from .models import Student
from django.http import HttpResponse


def feed_data(request):
    faker = Faker()
    for i in range(1000):
        name = faker.name()
        city = faker.city()
        roll = faker.pyint(min_value=1, max_value=1000)
        returned_data = Student.objects.get_or_create(name=name, city=city, roll=roll)
        print("Returned Data Type: ", type(returned_data))
        print("Actual Returned Data:", returned_data)
    return HttpResponse(json.dumps({"Message": "Successfully loaded data"}), content_type='application/json')
