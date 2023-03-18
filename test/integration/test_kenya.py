from unittest import TestCase
from pyprembly.data.kenya import DataVerification




class TestKenya(TestCase):

    def setUp(self):
        self.Verification = DataVerification()
        self.reference = 'njfijfdjdf82292jjds'
        self.name = 'John Doe'


    
    def test_passport(self):
        response = self.Verification.passport(
            number='A2050900', 
            customer_name=self.name,
            customer_reference=self.reference
            )
        self.assertEqual(response['message'], "Information Validated") 


    # def test_drivers_license(self):
    #     response = self.Verification.drivers_license(
    #         number='DXG100', 
    #         customer_name=self.name,
    #         customer_reference=self.reference
    #         )
    #     self.assertEqual(response['message'], "Information Validated")


    def test_serial_number(self):
        response = self.Verification.serial_number(
            number='78901010', 
            customer_name=self.name,
            customer_reference=self.reference
            )
        self.assertEqual(response['message'], "Information Validated") 


    def test_alien_id(self):
        response = self.Verification.alien_id(
            number='828944', 
            customer_name='sdsd',
            customer_reference='122'
            )
        self.assertEqual(response['message'], "Information Validated") 


    def test_national_identity_number_new(self):
        response = self.Verification.national_identity_number_new(
            number='101010', 
            customer_name=self.name,
            customer_reference=self.reference
            )
        self.assertEqual(response['message'], "Information Validated") 


   

