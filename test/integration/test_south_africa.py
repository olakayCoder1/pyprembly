from unittest import TestCase
from http  import HTTPStatus
from prembly.biometrics.data.south_africa import DataVerification




class TestSouthAfrica(TestCase):

    def setUp(self):
        self.Verification = DataVerification()


    
    def test_passport(self):
        response = self.Verification.national_id(
            nationalid='0123474827482',
            dob='1985-01-20',
            firstname='Khayone',
            lastname='Lethabo' 
            )
        self.assertEqual(response['message'], "Information Validated") 
