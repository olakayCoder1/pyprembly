from unittest import TestCase
from unittest.mock import patch
from pyprembly.face import FaceVerification 
import pyprembly



class TestFace(TestCase):

    def setUp(self) -> None:
        self.Verification = FaceVerification()



    # def test_comparison(self):
    #     response = self.Verification.comparison(
    #         image_one='https://res.cloudinary.com/dh3i1wodq/image/upload/v1675417496/cbimage_3_drqdoc.jpg',
    #         image_two='https://res.cloudinary.com/dh3i1wodq/image/upload/v1677955197/face_image_tkmmwz.jpg'
    #     )
    #     self.assertEqual(response['detail'], "Verification Successfull")


    def test_face_id(self):
        response = self.Verification.face_id(
            image='https://asset.cloudinary.com/dh3i1wodq/a52b7d',
        )
        self.assertEqual(response['detail'], "Verification Successful")

