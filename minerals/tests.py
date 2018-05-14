from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Test",
            image_filename="test.jpg",
            image_caption="Thumb's up",
            group="Terminators",
            formula='T9000',
            strunz_classification="a",
            crystal_system="b",
            mohs_scale_hardness="c",
            luster="d",
            color="e",
            specific_gravity="f",
            cleavage="g",
            diaphaneity="h",
            crystal_habit="i",
            streak="j",
            optical_properties="k",
            refractive_index="l",
            crystal_symmetry="m",
            unit_cell="n"
        )
        self.assertIs(mineral.name, "Test")
        self.assertIn(mineral, Mineral.objects.all())


class MineralsViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Test",
            image_filename="test.jpg",
            image_caption="Thumb's up",
            group="Terminators",
            formula='T9000',
            strunz_classification="a",
            crystal_system="b",
            mohs_scale_hardness="c",
            luster="d",
            color="e",
            specific_gravity="f",
            cleavage="g",
            diaphaneity="h",
            crystal_habit="i",
            streak="j",
            optical_properties="k",
            refractive_index="l",
            crystal_symmetry="m",
            unit_cell="n"
        )

    def test_index_view(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertIn(self.mineral, resp.context['minerals'])

    def test_detail_view(self):
        resp = self.client.get(reverse(
            'detail', kwargs={'name': self.mineral.name}
        ))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertIn(
            self.mineral.group, resp.context['data'].values()
        )
        self.assertContains(resp, self.mineral.name)
        self.assertContains(resp, self.mineral.group)

    def test_random_mineral_detail_view(self):
        resp = self.client.get(reverse(
            'detail', kwargs={'name': 'random-mineral'}
        ))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertIn(
            self.mineral.group, resp.context['data'].values()
        )
        self.assertContains(resp, self.mineral.name)
        self.assertContains(resp, self.mineral.group)
