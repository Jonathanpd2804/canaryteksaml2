from django.test import TestCase
from django.urls import reverse


class HomeTests(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenido a mi aplicación Django!")
        print("TEST 1 OK")

class HelloWorldTests(TestCase):
    def test_hello_world_view(self):
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hola, mundo!")
        print("TEST 2 OK")




