from unittest import TestCase
from http  import HTTPStatus
from unittest.mock import patch
from prembly.biometrics.data.ghana import DataVerification




class TestGhana(TestCase):

    def setUp(self):
        self.Verification = DataVerification()


    
    # def test_drivers_license(self):
    #     response = self.Verification.drivers_license(number=908987373, dob='2020-02-03')
    #     self.assertEqual(response.status_code, HTTPStatus.Ok ) 
        
        

