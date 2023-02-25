

class Face:

    # api/v2/biometrics/merchant/face/


    def age_and_gender(image):
        """
        Get the age range and gender of a person in an image
        Params:
            image: face image URL(base64, png , jpeg )
        """

        url = 'age_and_gender'

        # method = Post


    def comparison(image_one, image_two):
        """
       compare two face images
        Params:
            image: face image URL(base64, png , jpeg )
            image: face image URL(base64, png , jpeg )
        """

        url = 'comparison'

        # method = Post


    def enrollment(last_name, first_name, face_image , email):
        """
        Enroll user
        Params:
            last_name: user last name
            first_name: user's first name
            email: user's email address
            face_image: image url of user's face( use the best practices to generate the image)
        """
        # api/v2/biometrics/merchant/user/enroll
        url = 'api/v2/biometrics/merchant/user/enroll'

        # method = Post

    def authentication(image ):
        """
        Authenticate user using face
        Params:
            image: image url of user's face( use the best practices to generate the image)
        """
        # api/v2/biometrics/merchant/user/enroll
        url = 'api/v2/biometrics/merchant/user/authenticate'

        # method = Post


    def face_id(image ):
        """
        Verify user identity user  against their registered image using their id card(Voters card, National ID, Card etc)
        Params:
            image: image url of user's id card to verify( use the best practices to generate the image)
        """
        # test data o whatsapp
        url = 'api/v2/biometrics/merchant/user/id_verification'

        # method = Post


    def liveliness_check(image ):
        """
        Authenticate user with liveliness check on face
        Params:
            image: image url of user's face( use the best practices to generate the image)
        """
        # api/v2/biometrics/merchant/face/liveliness_check
        url = 'api/v2/biometrics/merchant/face/liveliness_check'

        # method = Post

