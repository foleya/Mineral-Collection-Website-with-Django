from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image_filename = models.CharField(max_length=255, null=True)
    image_caption = models.CharField(max_length=255, null=True)

    # These fields ordered by which ones are most common.
    group = models.CharField(max_length=255, null=True)  # 0 Empty
    formula = models.CharField(max_length=255, null=True)  # 7 Empty
    category = models.CharField(max_length=255, null=True)  # 25 Empty
    strunz_classification = models.CharField(max_length=255, null=True)  # 68 Empty
    crystal_system = models.CharField(max_length=255, null=True)  # 76 Empty
    mohs_scale_hardness = models.CharField(max_length=255, null=True)  # 89 Empty
    luster = models.CharField(max_length=255, null=True)  # 103 Empty
    color = models.CharField(max_length=255, null=True)  # 116 Empty
    specific_gravity = models.CharField(max_length=255, null=True)  # 162
    cleavage = models.CharField(max_length=255, null=True)  # 174 Empty
    diaphaneity = models.CharField(max_length=255, null=True)  # 179 Empty
    crystal_habit = models.CharField(max_length=255, null=True)  # 188 Empty
    streak = models.CharField(max_length=255, null=True)  # 198 Empty
    optical_properties = models.CharField(max_length=255, null=True)  # 238 Empty
    refractive_index = models.CharField(max_length=255, null=True)  # 257 Empty
    crystal_symmetry = models.CharField(max_length=255, null=True)  # 330 Empty
    unit_cell = models.CharField(max_length=255, null=True)  # 330 Empty

