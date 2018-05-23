from django.test import TestCase
from django.utils import timezone
import datetime
from unittest import skip

from rota.models import Shift

# Create your tests here.

class ShiftModelTest(TestCase):

    def test_can_create_a_shift_and_save_it(self):
        current_time = timezone.now()
        shift = Shift.objects.create(start_time=current_time)
        shift.save()
        shift.full_clean() # should not raise

    def test_new_shift_saves_correct_date(self):
        now = timezone.now()
        shift = Shift.objects.create(start_time=now)
        shift_start = shift.start_time
        self.assertEqual(shift_start, now)

    def test_new_shift_default_uses_current_datetime(self):
        """
        Uses datetime delta with 100 ms leeway to check correct time.
        If using staging server may need to increase this to allow for
        round trip delay.
        """
        current_datetime =  timezone.now()
        shift = Shift.objects.create()
        shift_start = shift.start_time
        self.assertTrue(
            (shift_start - current_datetime) <= datetime.timedelta(0, 0, 100)
        )
