import sys

try:
    from django.db import models
except  Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()


class DateTimeBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class User(DateTimeBaseModel):
    # Fields
    username = models.CharField(max_length=255, unique=True)


class Source(DateTimeBaseModel):
    # Fields
    name = models.CharField(max_length=255, unique=True)


class Genre(DateTimeBaseModel):
    # Fields
    name = models.CharField(max_length=255, unique=True)

    # Relationship Fields
    source = models.ForeignKey(Source, on_delete=models.PROTECT)


class SubGenre(DateTimeBaseModel):
    # Fields
    name = models.CharField(max_length=255, unique=True)

    # Relationship Fields
    source = models.ForeignKey(Source, on_delete=models.PROTECT)


class Environment(DateTimeBaseModel):
    # Fields
    name = models.CharField(max_length=255, unique=True)


class ElementType(DateTimeBaseModel):
    # Fields
    name = models.CharField(max_length=255, unique=True)


class Element(DateTimeBaseModel):
    # Fields
    name = models.CharField(max_length=255, unique=True)

    # Relationship Fields
    element_type = models.ForeignKey(ElementType, on_delete=models.CASCADE)


class Song(DateTimeBaseModel):

    # Choices Attributes
    ENERGY_UNSURE = '0'
    ENERGY_LOW = '1'
    ENERGY_MEDIUM = '2'
    ENERGY_HIGH = '3'
    ENERGY_LEVEL_CHOICES = (
        (ENERGY_UNSURE, 'Unsure'),
        (ENERGY_LOW, 'Low'),
        (ENERGY_MEDIUM, 'Medium'),
        (ENERGY_HIGH, 'High'),
    )

    # Fields
    energy = models.CharField(max_length=2, choices=ENERGY_LEVEL_CHOICES, default=ENERGY_UNSURE)
    uri = models.CharField(max_length=255, unique=True)

    # Relationship Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    sub_genres = models.ManyToManyField(SubGenre)
    environments = models.ManyToManyField(Environment)
    elements = models.ManyToManyField(Element)
