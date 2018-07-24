from django.test import TestCase
from sala.models import Sala

class SalaTestCase(TestCase):
    def setUp(self):
        Sala.objects.create(nazwa="inna", opis="opis innej sali")
        Sala.objects.create(nazwa="jeszcze_inna", opis="opis jeszcze innej sali")

    def test_sala_if_created(self):

        inna = Sala.objects.get(nazwa="inna")
        jeszcze_inna = Sala.objects.get(nazwa="jeszcze_inna")
        self.assertEqual(inna.opis, "opis innej sali")
        self.assertEqual(jeszcze_inna.opis, "opis jeszcze innej sali")

