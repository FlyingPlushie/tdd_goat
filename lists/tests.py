from django.test import TestCase #type: ignore

class SmokeTest(TestCase):
    
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)