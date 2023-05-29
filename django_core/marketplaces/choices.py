from django.db import models


class SolutionType(models.TextChoices):
    FULL_SIZE = 'Full size', 'Full size'
    TWO_SIDED = 'Two-sided', 'Two-sided'


class LicenseType(models.TextChoices):
    OPEN_SOURCE = 'Open source', 'Open source'
    NON_PUBLIC = 'Non-public license', 'Non-public license'


class SolutionSourceLocationType(models.TextChoices):
    RIGHT = 'Right', 'Right'
    LEFT = 'Left', 'Left'
