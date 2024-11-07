import factory.fuzzy

from ..models import Course


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    title = factory.Faker('word')
    description = factory.Faker('sentence', nb_words=10)
    price = factory.fuzzy.FuzzyDecimal(low=1, high=9999, precision=2)
    duration = factory.fuzzy.FuzzyInteger(low=1, high=12)
