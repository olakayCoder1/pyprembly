from unittest import TestCase
from prembly.biometrics.data.nigeria import DataVerification 




class TestNin(TestCase):

    def setUp(self) -> None:
        self.number_nin = 553727287282
        self.number = 87654567765
        self.Nin = DataVerification(
            # prembly_app_id='3fbd33f3-fb9a-4219-a13a-49490e2ae9d2',
            # prembly_x_api_key='test_ucc8c5fyl6rl78idn3lqjp:ogINip3R6hrzzARkTI42vv13ybY',
            # api_version='v2',
            # environment='live'
        )


    def test_nin_slip(self):
        response = self.Nin.nin_slip(image='https://asset.cloudinary.com/dh3i1wodq/089761016db6dab086ca450bf2465898')
        # print(response)
        # self.assertEqual(response.status_code , 200)
        # self.assertEqual(response['detail'], "Verification Successful")

    # def test_nin_lookup(self):
    #     response = self.Nin.nin_lookup(self.number,self.number_nin)
    #     print(response)
    #     self.assertEqual(response.status_code , 200)




