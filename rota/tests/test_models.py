from django.test import TestCase
from django.utils import timezone

from rota.models import Shift

# Create your tests here.

class ShiftModelTest(TestCase):

    def test_can_create_a_shift_and_save_it(self):
        now = timezone.now().date
        shift = Shift.objects.create()
        shift.date = timezone.now().date
        self.assertEqual(shift.date, now)
