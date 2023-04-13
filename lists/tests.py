from django.test import TestCase #type: ignore
from django.urls import resolve #type: ignore
from lists.views import home_page #type: ignore

class HomePageTest(TestCase):
    
  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)
