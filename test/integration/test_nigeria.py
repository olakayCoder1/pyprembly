from unittest import TestCase
from unittest.mock import patch
from prembly.biometrics.data.nigeria import DataVerification 
import prembly



class TestNin(TestCase):

    def setUp(self) -> None:
        self.number_nin = 553727287282
        self.number = 87654567765
        self.Verification = DataVerification(
            # prembly_app_id='3fbd33f3-fb9a-4219-a13a-49490e2ae9d2',
            # prembly_x_api_key='test_ucc8c5fyl6rl78idn3lqjp:ogINip3R6hrzzARkTI42vv13ybY',
            # api_version='v2',
            # environment='live'
        )


    # def test_nin_slip(self):
    #     response = self.Nin.nin_slip(image='https://asset.cloudinary.com/dh3i1wodq/089761016db6dab086ca450bf2465898')
    #     print(response)
    #     self.assertEqual(response.status_code , 200)
    #     self.assertEqual(response['detail'], "Verification Successful")


    @patch('prembly.biometrics.data.nigeria.DataVerification.nin_lookup')
    def test_nin_lookup(self, mock_data ):
        mock_data.return_value = {'foo':'bar'}
        response = self.Verification.nin_lookup(self.number,self.number_nin)
        # print(response)
        self.assertEqual(response['foo'] , 'bar')



    def test_vehicle(self):
        response = self.Verification.plate_number(vehicle_number='AAA000000')
        self.assertEqual(response , 200)





