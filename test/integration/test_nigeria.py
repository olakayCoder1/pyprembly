from unittest import TestCase
from unittest.mock import patch
from prembly.data.nigeria import DataVerification 
import prembly



class TestNigeria(TestCase):

    def setUp(self) -> None:
        self.Verification = DataVerification()



    def test_cac(self):
        response = self.Verification.cac(
            rc_number='092932',
            company_type='RC'
        )
        self.assertEqual(response['detail'], "Verification Successfull")



    def test_cac_advance(self):
        response = self.Verification.cac_advance(
            company_name='TEST COMPANY',
            company_type='RC',
            rc_number='092932'
        )
        self.assertEqual(response['detail'], "Verification Successfull")


    # def test_cac_with_name(self):
    #     response = self.Verification.cac_with_name(
    #         company_name='TEST COMPANY'
    #     )
    #     self.assertEqual(response['detail'], "Verification Successful")


    def test_phone_number(self):
        response = self.Verification.phone_number(
            number='08082838283'
        )
        self.assertEqual(response['detail'], "Verification Successfull")


    def test_banks_code(self):
        response = self.Verification.banks_code()
        self.assertEqual(response["message"], "Data Retreived")

    def test_bank_account(self):
        response= self.Verification.bank_account(
            number=4444444444,
            bank_code=214
        )
        self.assertEqual(response['detail'], "Verification Successful")
        
    
    def test_voters_card_lookup(self):
        response = self.Verification.voters_card_lookup(
            number= '987f545AJ67890',
            last_name= 'test' ,
            state= 'Lagos'
        )
        self.assertEqual(response['detail'], "VIN Verification Successful")

    def test_basic_drivers_license(self):
        response = self.Verification.basic_drivers_license(
            number='AAD23208212298',
            dob='1999-12-21',
            first_name='test',
            last_name='test'
        )
        self.assertEqual(response['detail'], "DL Verification Successfull")


    def test_advance_drivers_license(self):
        response = self.Verification.advance_drivers_license(
            number='AAD23208212298',
            dob='1999-12-21',
            first_name='test',
            last_name='test'
        )
        self.assertEqual(response['detail'], "DL Verification Successful")

    def test_drivers_license_image(self):
        response = self.Verification.drivers_license_image(
            image='https://res.cloudinary.com/dh3i1wodq/image/upload/v1675417496/cbimage_3_drqdoc.jpg',
            number='AAD23208212298',
            dob='1999-12-21'
        )
        self.assertEqual(response['detail'], "DL Verification Successful")


    def test_international_passport(self):
        response = self.Verification.international_passport(
            number='A00400000',
            last_name='test'
        )
        self.assertEqual(response['detail'], "Verification Successfull")


    def test_credit_bureau(self):
        response = self.Verification.credit_bureau(
            phone_number='08080808080',
            first_name='test'
        )
        self.assertEqual(response['detail'], "Credit Verification Successful")


    def test_credit_bureau_customer(self):
        response = self.Verification.credit_bureau_customer(
            customer_reference='jhgfdfghbvgjhgf',
            customer_name= 'Test Name',
            mode='ID',
            number='11111111111',
            dob='1990-08-01',
            
        )
        self.assertEqual(response['detail'], "Credit Check successful")


    def test_credit_bureau_commercial_basic(self):
        response = self.Verification.credit_bureau_commercial_basic(
            customer_name='Test Name',
            rc_number='59002',
            customer_reference='jhgfdfghbvgjhgf'
        )
        self.assertEqual(response['detail'], "Credit Check successful")



    def test_credit_bureau_commercial(self):
        response = self.Verification.credit_bureau_commercial(
            customer_name='Test Name',
            rc_number='59001',
            customer_reference='jhgfdfghbvgjhgf'
        )
        self.assertEqual(response['detail'], "Credit Check successful")





    def test_nin_slip(self):
        response = self.Verification.nin_slip(image='https://asset.cloudinary.com/dh3i1wodq/089761016db6dab086ca450bf2465898')
        self.assertEqual(response['detail'], "Verification Successful")

    def test_nin_virtual(self):
        response = self.Verification.nin_virtual(
            number='AA1234567890123B',
            number_nin='12345678909'
        )
        self.assertEqual(response['detail'], "Verification Successfull")


    def test_nin_face(self):
        response = self.Verification.nin_face(
            number='12345678909',
            image='https://res.cloudinary.com/dh3i1wodq/image/upload/v1675417496/cbimage_3_drqdoc.jpg'
        )
        self.assertEqual(response['detail'], "Verification Successfull")

    # def test_bvn(self):
    #     response = self.Verification.bvn_with_face(
    #         number= 54651333604,
    #         image='https://www.biography.com/.image/c_fill%2Ccs_srgb%2Cfl_progressive%2Ch_400%2Cq_auto:good%2Cw_620/MTY2MzU3Nzk2OTM2MjMwNTkx/elon_musk_royal_society.jpg',
    #     )
    #     self.assertEqual(response['detail'], "Verification Successful")

    
    def test_bvn_number(self):
        response = self.Verification.bvn_number(
            number= 54651333604,
        )
        self.assertEqual(response['detail'], "Verification Successful")

    @patch('prembly.biometrics.data.nigeria.DataVerification.nin_lookup')
    def test_nin_lookup(self, mock_data ):
        mock_data.return_value = {'foo':'bar'}
        response = self.Verification.nin_lookup('54651333604','54651333604')
        self.assertEqual(response['foo'] , 'bar')



    def test_vehicle_verification(self):
        response = self.Verification.vehicle_verification(
            vehicle_number='AAA000000'
            )
        self.assertEqual(response['detail'] , "Vehicle Verification Successful" )






