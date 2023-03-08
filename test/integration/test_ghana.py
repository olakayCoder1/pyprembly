from unittest import TestCase
from http  import HTTPStatus
from prembly.biometrics.data.ghana import DataVerification




class TestGhana(TestCase):

    def setUp(self):
        self.Verification = DataVerification()


    
    def test_drivers_license(self):
        response = self.Verification.drivers_license(number=908987373, dob='2020-02-03')
        self.assertEqual(response['detail'], "Drivers License  Verification failed") 

    def test_international_passport(self):
        response = self.Verification.international_passport(number='G0000575')
        self.assertEqual(response['detail'], "Passport Verification Successful")


    # def test_ssnit(self):
    #     response = self.Verification.ssnit(number='C987464748983')
    #     self.assertEqual(response['detail'], "Passport Verification Successful")

    
    # def test_voters_card(self):
    #     response = self.Verification.voters_card(type='MAIN', number='9001332866')
    #     self.assertEqual(response['detail'], "Passport Verification Successful")
        
        

