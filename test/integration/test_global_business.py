from unittest import TestCase
from http  import HTTPStatus
from prembly.business import DataVerification 




class TestGlobalBusiness(TestCase):

    def setUp(self):
        self.Verification = DataVerification()


    
    def test_search_company(self):
        response = self.Verification.search_company(
            country_code='ng',
            company_name='Test Company',
            )
        self.assertEqual(response['detail'], "Companies Retrieved Successfully") 


    def test_vin_verification(self):
        response = self.Verification.vin_verification(
            vin='AAA00000000'
            )
        self.assertEqual(response['detail'], "VIN Verification Successful") 

    
    def test_verify_company(self):
        response = self.Verification.verify_company(
           company_number='1000010',
           country_code='ng',
           customer_name='test',
           customer_reference='jhbgywywuwhbhshbsnvs'
            )
        self.assertEqual(response['detail'], "Companies Retrieved Successfully") 