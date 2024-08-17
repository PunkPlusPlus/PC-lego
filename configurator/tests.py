from django.test import TestCase

from configurator.models import Component, ComponentTypes

from configurator.services import AssemblyBuilder


class AssemblyBuilderTestCase(TestCase):
    fixtures = ['Brands.json', 'Components.json']

    def setUp(self):
        self.builder = AssemblyBuilder()

    def test_success_setting_components(self):
        card = Component.objects.filter(type=ComponentTypes.VIDEO_CARD.value).first()
        self.builder.set_video_card(card)


