from prembly.base import BaseConfig
from prembly.exceptions import *
from prembly.utils import create_request_url


class Nin(BaseConfig):


    def verify_slip(self, image=None) :
        """
        Verify a National Identification Number(NIN) Slip
        image : Nin slip image 
        """
        if not image:
            raise MissingRequiredDataError('Required data "image" not provided')
        verify_url = self._BASE_END_POINT_VERSION + '/biometrics/merchant/data/verification/nin/image'
        url = create_request_url(url=verify_url) 
        self._handle_request('POST', url , data=image)



    def verify_lookup(self, number=None , number_nin=None) :
        """
        Verify a National Identification Number(NIN) with phone number and (NIN) number
        number : Phone number used for nin registration
        number_nin : Nin registration number
        """
        data = {} 
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        else:
            data.update({'number': number} )
        if not number:
            raise MissingRequiredDataError('Required data "nin" not provided')
        else:
            data.update({'number_nin': number_nin} ) 

        verify_url = self._BASE_END_POINT_VERSION + '/biometrics/merchant/data/verification/nin_wo_face'

        url = create_request_url(url=verify_url) 
        self._handle_request('POST', url , data=data)



    def verify_virtual(self, number=None , number_nin=None) :
        """
        Verify a National Identification Number(NIN) with NIN and virtual number
        number : Virtual nin number
        number_nin : Nin registration number 
        Note:
            The Virtual NIN (vNIN) is designed to replace the raw 11-digit NIN for everyday usage.
            Where until now, the raw NIN had been shared and stored by various entities mostly without the knowledge (or consent) of the ID Holder or the Custodian of Identity in Nigeria, the NIMC.\n
            Virtual NIN consists of 16 alpha-numeric characters that can be generated using:\n
            NIMC official mobile app\n
            USSD - _346_3_customer NIN_696739#\n
            Identitypass Short Code: 696739
            
        """
        data = {} 
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        else:
            data.update({'number': number} )
        if not number:
            raise MissingRequiredDataError('Required data "nin" not provided')
        else:
            data.update({'number_nin': number_nin} ) 

        verify_url = self._BASE_END_POINT_VERSION + '/biometrics/merchant/data/verification/nin_wo_face'

        url = create_request_url(url=verify_url) 
        self._handle_request('POST', url , data=data)


    
    def verify_face(self, number=None , image=None) :
        """
        Verify a National Identification Number(NIN) with user's image
        number : Virtual nin number
        image : Image url     
            
        """
        data = {} 
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        else:
            data.update({'number': number} )
        if not image:
            raise MissingRequiredDataError('Required data "image" not provided')
        else:
            data.update({'image': image} ) 

        verify_url = self._BASE_END_POINT_VERSION + '/biometrics/merchant/data/verification/nin'

        url = create_request_url(url=verify_url) 
        self._handle_request('POST', url , data=data)





















