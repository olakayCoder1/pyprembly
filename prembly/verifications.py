from .base import BaseConfig
from prembly.exceptions import *
from prembly.utils import create_request_url



class Verification(BaseConfig):

    
    def cac(self, rc_number: int = None , company_type : str ='RC' ):
        """
        Verify a business using rc_number
        rc_number : The registration number of company\n
        company_type : company type : default - > RC
        """
        data = {'company_type': company_type}
        # 092932
        # TEST COMPANY
        if not rc_number:
            raise MissingRequiredDataError('Required data "rc_number" not provided')
        data.update(
            {
                'rc_number': rc_number
            }
        )
        verify_url = self._BASE_END_POINT_VERSION + '/cac'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data)


    def cac_with_name(self,company_name : str = None ):
        """
        Verify a business using rc_number
        company_name : The company name
        """
        data = {'company_type': company_name}
        # 092932
        # TEST COMPANY
        if not company_name:
            raise MissingRequiredDataError('Required data "rc_number" not provided')
        data.update(
            {
                'company_name': company_name
            }
        )
        verify_url = self._BASE_END_POINT_VERSION + '/cac_w_name'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data)


    
    def cac_advance(self,  rc_number: int = None ,  company_type : str ='RC' , company_name : str = None ):
        """
        Verify a business using rc_number
        rc_number : The registration number of company
        company_type : company type : default - > RC
        company_name : The company name
        """
        data = {'company_type': company_type }
        # 092932
        # TEST COMPANY
        if not rc_number:
            raise MissingRequiredDataError('Required data "rc_number" not provided')
        
        if not company_name:
            raise MissingRequiredDataError('Required data "rc_number" not provided')
        data.update(
            {
                'rc_number': rc_number , 'company_name': company_name
            }
        )
        verify_url = self._BASE_END_POINT_VERSION + '/cac/advance'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data)


    def bvn_number(self, number: int = None ):
        """
        Verify a Bank Verification Number (BVN)
        number : Bank Verification Number
        """
        data = {}
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        data.update({ 'number': number })
        verify_url = self._BASE_END_POINT_VERSION + '/bvn'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data)


    def bvn_with_face(self, number: int = None , image: str = None ):
        """
        Verify a Bank Verification Number (BVN)
        number : Bank Verification Number
        image : Image url(png, jpeg , base64)
        """
        data = {}
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
     
        if not image:
            raise MissingRequiredDataError('Required data "image" not provided')
        data.update(
            {
                'image': image , 'number': number
            }
        )
        verify_url = self._BASE_END_POINT_VERSION + '/bvn_w_face'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data)

    
    def phone_number_verification(self, number: int = None , v_type:str='normal'):
        """
        Verify a Phone Number
        number : Phone number\n
        v_type : Phone number verification type eg advance or normal : default - > normal
        """
        data = {}
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        data.update(
            {
                'number': number
            }
        )
        verify_url = self._BASE_END_POINT_VERSION + '/phone_number'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data)


    def banks_code(self):
        """
        Get all banks code
        """
        verify_url = self._BASE_END_POINT_VERSION + '/bank_code'
        url = create_request_url(url=verify_url) 
        return self._handle_request('GET', url )


    def bank_account_verification(self , number:int=None,bank_code:str=None):
        """
        Verify bank account number
        number : bank account number
        bank_code : code of the user's bank
        """
        data = {}
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        if not bank_code:
            raise MissingRequiredDataError('Required data "bank_code" not provided')
        data.update(
            {
                'bank_code': bank_code ,  'number': number
            }
        )
        verify_url = self._BASE_END_POINT_VERSION + '/bank_account'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )

    
    def advance_bank_account_verification(self , number:int=None,bank_code:str=None):
        """
        Verify bank account number
        number : bank account number
        bank_code : code of the user's bank
        """
        data = {}
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        if not bank_code:
            raise MissingRequiredDataError('Required data "bank_code" not provided')
        data.update(
            {
                'bank_code': bank_code ,  'number': number
            }
        )
        verify_url = self._BASE_END_POINT_VERSION + '/bank_account/advance'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    def bank_account_with_name_verification(
        self , number:int=None,bank_code:str=None , 
        customer_name:str=None , customer_reference:str=None):
        """
        Verify bank account number
        number : bank account number
        bank_code : code of the user's bank
        customer_name : your customer name
        customer_reference : your customer reference
        """
        data = {}
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        if not bank_code:
            raise MissingRequiredDataError('Required data "bank_code" not provided')
        data.update(
            {
                'bank_code': bank_code ,  'number': number ,
                 'customer_reference': customer_reference,
                 'customer_name':customer_name
            }
        )
        verify_url = self._BASE_END_POINT_VERSION + '/bank_account/comparism'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )



    def voters_card_image_verification(self , image:str=None):
        """
        Verify voters card ID image
        image : voters card image(png,jpg, base64)
        """
        data = {}
        if not image:
            raise MissingRequiredDataError('Required data "image" not provided')

        data.update(
            {
                'image': image ,
            }
        )
        verify_url = self._BASE_END_POINT_VERSION + '/voters_card/image'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )

    
    def voters_card_lookup_verification(self , number:int=None , state:str=None , last_name:str=None):
        """
        Verify voters card number
        number : voters card number
        state : state
        last_name : last name
        """
        #987f545AJ67890
        #test
        #Lagos
        data = {}
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        if not state:
            raise MissingRequiredDataError('Required data "state" not provided')
        if not last_name:
            raise MissingRequiredDataError('Required data "last_name" not provided')

        data.update(
            {
                'number': number , 'state': state , 'last_name' : last_name
            }
        )
        verify_url = self._BASE_END_POINT_VERSION + '/voters_card'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )

    

    def basic_drivers_license_verification(
        self , number:int=None , dob:str=None , 
        first_name:str=None, last_name:str=None):
        """
        Verify drivers license
        number : license number
        dob : date of birth
        first_name : first name
        last_name : last name
        """
        #AAD23208212298
        #1999-12-21
        #test
        #test
        data = {}
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        if not dob:
            raise MissingRequiredDataError('Required data "dob" not provided')
        if not first_name:
            raise MissingRequiredDataError('Required data "first_name" not provided')
        if not last_name:
            raise MissingRequiredDataError('Required data "last_name" not provided')
        
        data.update(
            {
                'number': number , 'dob' : dob, 
                'first_name' : first_name, 'last_name' : last_name
            }
        )
    
        verify_url = self._BASE_END_POINT_VERSION + '/drivers_license/basic'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    def advance_drivers_license_verification(
        self , number:int=None , dob:str=None , 
        first_name:str=None, last_name:str=None):
        """
        Verify drivers license
        number : license number
        dob : date of birth
        first_name : first name
        last_name : last name
        NOTE : dob format should look like 1998-06-19 - Format)
        """
        #AAD23208212298
        #1999-12-21
        #test
        #test
        data = {}
        if not number:
            raise MissingRequiredDataError('Required data "number" not provided')
        if not dob:
            raise MissingRequiredDataError('Required data "dob" not provided')
        if not first_name:
            raise MissingRequiredDataError('Required data "first_name" not provided')
        if not last_name:
            raise MissingRequiredDataError('Required data "last_name" not provided')
        
        data.update(
            {
                'number': number , 'dob' : dob, 
                'first_name' : first_name, 'last_name' : last_name
            }
        )
    
        verify_url = self._BASE_END_POINT_VERSION + '/drivers_license/advance'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    def image_drivers_license_verification(self ,  image:str=None):
        """
        Verify drivers license ID image
        image : License image
        """
        if not image:
            raise MissingRequiredDataError('Required data "image" not provided')
        
        data  = {'image' : image }
        
    
        verify_url = self._BASE_END_POINT_VERSION + '/drivers_license/image'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    def image_drivers_license_verification(self , number:int=None,  dob:str=None ,  image:str=None):
        """
        Verify drivers license ID image
        number : FRSC number
        dob : date of birth
        image : image(png,jpg, base64)
        """        
        data  = {'image' : image , 'number': number , 'dob' : dob,  }
    
        verify_url = self._BASE_END_POINT_VERSION + '/drivers_license_with_face'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    
    def national_passport_verification(self , number:int=None,  last_name:str=None):
        """
        Verify international passport
        number : passport number
        last_name : user's last name
        """        
        data  = { 'number': number , 'last_name' : last_name,  }
    
        verify_url = self._BASE_END_POINT_VERSION + '/national_passport'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    
    def national_passport_image_verification(self , image:str=None,  customer_reference:str=None , customer_name:str=None):
        """
        Verify international passport image 
        customer_reference : unique customer reference
        customer_name : customer name
        image : passport image(png,jpg, base64)
        """        
        data  = { 'image': image , 'customer_reference' : customer_reference,'customer_name' : customer_name,  }
    
        verify_url = self._BASE_END_POINT_VERSION + '/national_passport_image'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    def national_passport_with_face_verification(self , image:str=None,  last_name:str=None , number:int=None):
        """
        Verify international passport image 
        last_name : user's last name
        number : passport number
        image :  image(png,jpg, base64)
        """        
        data  = { 'image': image , 'last_name' : last_name,'number' : number,  }
    
        verify_url = self._BASE_END_POINT_VERSION + '/national_passport_with_face'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    def national_passport_async_verification(self , last_name:str=None , number:int=None):
        """
        Verify international passport in an asynchronous manner. The passport details will be verified and send later to your webhook url
        NOTE : configure your webhook URL before using this function
        last_name : user's last name
        number : passport number
        """        
        data  = { 'last_name' : last_name,'number' : number,  }
    
        verify_url = self._BASE_END_POINT_VERSION + '/national_passport/async'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    
    def credit_bureau_verification(
        self, customer_reference, 
        customer_name:str=None , number:int=None, mode:str=None , dob:str=None
        ):
        """
        Verify advance credit details of a user
        customer_reference : unique customer reference
        customer_name : customer name
        number : if model is ID(should be BVN)
        dob : if model is BIO(Date of birth)
        mode : either ID or BVN
        """        
        data  = { 
            'customer_name' : customer_name, 
            'customer_reference' : customer_reference ,
            'number' : number,  'dob': dob  , 'mode' : mode
        }
    
        verify_url = self._BASE_END_POINT_VERSION + '/credit_bureau/customer/advance'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )

    
    def credit_bureau_commercial_verification(
        self, customer_reference, 
        customer_name:str=None , rc_number:int=None
        ):
        """
        Verify advance credit details of a business
        rc_number : company RC number
        customer_name : customer  name
        customer_reference : unique customer reference
        """        
        data  = { 
            'customer_name' : customer_name, 
            'customer_reference' : customer_reference ,
            'rc_number' : rc_number
        }
    
        verify_url = self._BASE_END_POINT_VERSION + '/credit_bureau/commercial/advance'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    def credit_bureau_commercial_basic_verification(
        self,customer_name:str=None , rc_number:int=None ):
        """
        Verify basic credit details of a business
        rc_number : company RC number
        customer_name : customer  name
        """        
        data  = { 
            'customer_name' : customer_name, 
            'rc_number' : rc_number
        }
    
        verify_url = self._BASE_END_POINT_VERSION + '/credit_bureau/commercial/basic'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )


    def credit_bureau_statement(
        self,first_name:str=None ,phone_number:int=None ):
        """
        Verify basic credit details of a business
        phone_number : Phone number
        first_name : first name
        """        
        data  = { 
            'first_name' : first_name, 
            'phone_number' : phone_number
        }
    
        verify_url = self._BASE_END_POINT_VERSION + '/credit_bureau/commercial/basic'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data )




