"""
Premby API wrapper.

@author Olanrewaju Kabiru.

"""
from prembly.utils import image_to_base64
from prembly.base import PremblyBase


class FaceVerification(PremblyBase):


    def _face_base_endpoint(self):
        return self._BASE_END_POINT + '/api/v2/biometrics/merchant/face'


    def age_and_gender(self, image):
        """
        Get the age range and gender of a person in an image
        
        Params:
            image: face image URL(base64, png , jpeg )
        """
        if image:
            image = image_to_base64(image)
        data = {'image':image}
        url = self._face_base_endpoint() +  '/age_and_gender'
        return self._handle_request('POST', url , data )
    

    def comparison(self, image_one, image_two):
        """
       compare two face images

        Params:
            image_one: face image URL(base64, png , jpeg )
            image_two: face image URL(base64, png , jpeg )
        """
        # if image_one and image_two:
        #     image_one = image_to_base64(image_one)
        #     image_two = image_to_base64(image_two)
        data = {
            'image_one':image_one,
            'image_two':image_two
        }
        url = self._face_base_endpoint() + '/comparison'

        return self._handle_request('POST', url , data )


    def enrollment(self, last_name, first_name, face_image , email):
        """
        Enroll user

        Params:
            last_name: user last name
            first_name: user's first name
            email: user's email address
            face_image: image url of user's face( use the best practices to generate the image)
        """
        if face_image:
            face_image = image_to_base64(face_image)
        data={
            'last_name':last_name , 
            'first_name':first_name , 
            'face_image':face_image , 
            'email':email
        }
        url = self._BASE_END_POINT + 'api/v2/biometrics/merchant/user/enroll'
        return self._handle_request('POST', url , data )
        # method = Post


    def authentication(self, image ):
        """
        Authenticate user using face

        Params:
            image: image url of user's face( use the best practices to generate the image)
        """
        if image:
            image = image_to_base64(image)
        data={'image':image }
        url = self._BASE_END_POINT + 'api/v2/biometrics/merchant/user/authenticate'
        return self._handle_request('POST', url , data )
        # method = Post


    def face_id(self, image ):
        """
        Verify user identity user  against their registered image using their id card(Voters card, National ID, Card etc)

        Params:
            image: image url of user's id card to verify( use the best practices to generate the image)
        """
        # if image:
        #     image = image_to_base64(image)
        data={'image': image  }
        # test data o whatsapp
        url = self._BASE_END_POINT + '/api/v2/biometrics/merchant/user/id_verification'
        return self._handle_request('POST', url , data )
        # method = Post


    def liveliness_check(self, image ):
        """
        Authenticate user with liveliness check on face

        Params:
            image: image url of user's face( use the best practices to generate the image)
        """
        if image:
            image = image_to_base64(image)
        data={'image':image  }
        url = self._BASE_END_POINT + 'api/v2/biometrics/merchant/face/liveliness_check'
        return self._handle_request('POST', url , data )
        # method = Post
        