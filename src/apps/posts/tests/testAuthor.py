from django.test import TestCase
from ..models import Author


class PostTestCase(TestCase):
    
    def testAuthor(self):
        author = Author(
            full_name="Rafin Rashid", 
            phone_number="0000000", 
            email="rafin@gmail.com",
            address="Sylhet, Bangladesh"
        )
        self.assertEqual(author.full_name, "Rafin Rashid")
        self.assertEqual(author.phone_number, "0000000")
        self.assertEqual(author.email, "rafin@gmail.com")
        self.assertEqual(author.address, "Sylhet, Bangladesh")