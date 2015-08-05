from django.test import TestCase
from .models import *
from django.core.urlresolvers import reverse

TESTING_NAME = "__test__"

class SpellTests(TestCase):
    def setUp(self):
        self.instance = Spell.objects.create(name = TESTING_NAME,
                                 is_ritual = False,
                                 is_concentration=False,
                                 level = 1,
                                 school = "Evocation",
                                 casting_time = "1 action",
                                 duration = "Instantaneous",
                                 range = "30 feet",
                                 description = "This is only a test.",
                                 at_higher_levels = "")

    def tearDown(self):
        Spell.objects.filter(name__exact = TESTING_NAME).delete()

    def test_spell_creation(self):
        self.assertTrue(isinstance(self.instance, Spell))
        self.assertEqual(str(self.instance), self.instance.name)
        self.assertFalse(self.instance.is_ritual)
        self.assertFalse(self.instance.is_concentration)

    def test_spell_list_view(self):
        url = reverse("Spell_List.views.index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

class ComponentTests(TestCase):

    def setUp(self):
        self.instance = Component.objects.create(name = TESTING_NAME, abbreviation = "T")

    def tearDown(self):
        Component.objects.filter(name__exact = TESTING_NAME).delete()

    def test_component_creation(self):
        self.assertTrue(isinstance(self.instance, Component))
        self.assertEqual(str(self.instance), self.instance.name)
