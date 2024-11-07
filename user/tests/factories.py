import factory.fuzzy

from ..models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password', length=10)
    balance = factory.fuzzy.FuzzyDecimal(low=0, high=9999, precision=2)

    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for course in extracted:
                self.courses.add(course)
