from django.test import TestCase
import datetime

from django.utils import timezone
from django.urls import reverse

from .models import Poll


class PollModelTest(TestCase):
    def test_was_published_recently_with_future_poll(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_poll = Poll(pub_date=time)
        self.assertIs(future_poll.was_published_recently(), False)

        """
      was_published_recently() returns False for polls whose pub_date
      is older than 1 day.
       """


class PollModelTest2(TestCase):
    def test_was_published_recently_with_old_poll(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_poll = Poll(pub_date=time)
        self.assertIs(old_poll.was_published_recently(), False)



# Create your tests here.
