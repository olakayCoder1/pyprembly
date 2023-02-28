from unittest import TestCase
from unittest.mock import patch
from prembly.biometrics.data.nigeria import DataVerification 
import prembly



class TestNin(TestCase):

    def setUp(self) -> None:
        self.Verification = DataVerification()


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
        self.assertEqual(response['detail'], "Verification Successful")

    def test_bvn(self):
        response = self.Verification.bvn_with_face(
            number= 54651333604,
            image='https://www.biography.com/.image/c_fill%2Ccs_srgb%2Cfl_progressive%2Ch_400%2Cq_auto:good%2Cw_620/MTY2MzU3Nzk2OTM2MjMwNTkx/elon_musk_royal_society.jpg',
        )
        self.assertEqual(response['detail'], "Verification Successful")

    
    def test_bvn_number(self):
        response = self.Verification.bvn_number(
            number= 54651333604,
        )
        self.assertEqual(response['detail'], "Verification Successful")

    @patch('prembly.biometrics.data.nigeria.DataVerification.nin_lookup')
    def test_nin_lookup(self, mock_data ):
        mock_data.return_value = {'foo':'bar'}
        response = self.Verification.nin_lookup(self.number,self.number_nin)
        # print(response)
        self.assertEqual(response['foo'] , 'bar')



    def test_vehicle_verification(self):
        response = self.Verification.vehicle_verification(
            vehicle_number='AAA000000'
            )
        self.assertEqual(response['detail'] , "Vehicle Verification Successful" )






