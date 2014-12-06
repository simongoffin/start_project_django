from django.test import TestCase

# Create your tests here.

from views import home
from Algo.Run import run
from django.core.urlresolvers import reverse
from django.test import Client


class CalculTests(TestCase):
    def test_home(self):
        data={'x':1 , 'y':2}
        response = self.client.get(reverse('application.views.home'),data)
        self.assertEqual(response.status_code, 200)
    
    def test_run(self):
        z=run(1,2)
        self.assertEqual(z, 3)




