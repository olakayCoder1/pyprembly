from prembly.base import BaseConfig
from prembly.exceptions import *
from prembly.utils import create_request_url



class Verification(BaseConfig):
    """
    Base class for all IdentityPass API available in Nigeria
    """
    
    @classmethod
    def cac(cls, rc_number: int = None , company_type : str ='RC' ):
        """
        Verify a business using rc_number
        
        Args:
            rc_number : The registration number of company

            company_type : company type : default - > RC
        Returns : 
            Json data from Prembly API.
        """
        data = {'company_type': company_type , 'rc_number': rc_number}
        url = cls.create_request_url(suburl='/cac') 
        return cls._handle_request('POST', url , data=data)

    @classmethod
    def cac_with_name(cls,company_name : str = None ):
        """
        Verify a business using rc_number
        company_name : The company name
        Args:
            company_name : The company name
        Returns : 
            Json data from Prembly API.
        """
        # 092932
        # TEST COMPANY
        data = {'company_type': company_name ,'company_name': company_name}
        verify_url = cls._BASE_END_POINT_VERSION + '/cac_w_name'
        url = cls.create_request_url(suburl=verify_url) 
        return cls._handle_request('POST', url , data=data)


    @classmethod
    def cac_advance(cls,  rc_number: int = None ,  company_type : str ='RC' , company_name : str = None ):
        """
        Verify a business using rc_number
        
        Args:
            rc_number : The registration number of company

            company_type : company type : default - > RC
            company_name : The company name
        Returns : 
            Json data from Prembly API.
        """
        # 092932
        # TEST COMPANY
        data = {'company_type': company_type , 'rc_number': rc_number , 'company_name': company_name }
        url = cls.create_request_url(suburl='/cac/advance') 
        return cls._handle_request('POST', url , data=data)

    @classmethod
    def bvn_number(cls, number: int = None ):
        """
        Verify a Bank Verification Number (BVN)
        number : Bank Verification Number
        Args:
            number : Bank Verification Number
        Returns : 
            Json data from Prembly API.
        """
        data = { 'number': number }
        url = cls.create_request_url(suburl='/bvn') 
        return cls._handle_request('POST', url , data=data)

    @classmethod
    def bvn_with_face(cls, number: int = None , image: str = None ):
        """
        Verify a Bank Verification Number (BVN) using image and number
       
        Args:
            number : Bank Verification Number
            image : Image url(png, jpeg , base64)
        Returns : 
            Json data from Prembly API.
        """
        data = { 'image': image , 'number': number  }
        url = cls.create_request_url(suburl='/bvn_w_face') 
        return cls._handle_request('POST', url , data=data)

    @classmethod
    def phone_number(cls, number: int = None , v_type:str='normal'):
        """
        Verify a Phone Number
        
        Args:
            number : Phone number

            v_type : Phone number verification type eg advance or normal : default - > normal
        Returns : 
            Json data from Prembly API.
        """
        data = {'number': number }
        url = cls.create_request_url(suburl='/phone_number') 
        return cls._handle_request('POST', url , data=data)

    @classmethod
    def banks_code(cls):
        """
        Get all banks code
        """
        url = cls.create_request_url(suburl='/bank_code') 
        return cls._handle_request('GET', url )

    @classmethod
    def bank_account(cls , number:int=None,bank_code:str=None):
        """
        Verify bank account number
        
        Args:
            number : bank account number
            bank_code : code of the user's bank
        Returns : 
            Json data from Prembly API.
        """
        data = {
                'bank_code': bank_code ,  'number': number
            }
        url = cls.create_request_url(suburl='/bank_account') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def advance_bank_account(cls , number:int=None,bank_code:str=None):
        """
        Verify bank account number
        
        Args:
            number : bank account number
            bank_code : code of the user's bank
        Returns : 
            Json data from Prembly API.
        """
        data = {'bank_code': bank_code ,  'number': number}
        url = cls.create_request_url(suburl='/bank_account/advance') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def bank_account_with_name(
        cls , number:int=None,bank_code:str=None , 
        customer_name:str=None , customer_reference:str=None):
        """
        Verify bank account number
        
        Args:
            number : bank account number
            bank_code : code of the user's bank
            customer_name : your customer name
            customer_reference : your customer reference
        Returns : 
            Json data from Prembly API.
        """
        data = {'bank_code': bank_code ,  'number': number ,
                 'customer_reference': customer_reference,
                 'customer_name':customer_name
                }
        url = cls.create_request_url(suburl='/bank_account/comparism') 
        return cls._handle_request('POST', url , data=data )


    @classmethod
    def voters_card_image(cls , image:str=None):
        """
        Verify voters card ID image
        
        Args:
            image : voters card image(png,jpg, base64)
        Returns : 
            Json data from Prembly API.
        """
        data = {'image': image }
        url = cls.create_request_url(suburl='/voters_card/image') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def voters_card_lookup(cls , number:int=None , state:str=None , last_name:str=None):
        """
        Verify voters card number
        
        Args:
            number : voters card number
            state : state
            last_name : last name
        Returns : 
            Json data from Prembly API.
        """
        #987f545AJ67890
        #test
        #Lagos
        data = { 'number': number , 'state': state , 'last_name' : last_name}
        url = cls.create_request_url(suburl='/voters_card') 
        return cls._handle_request('POST', url , data=data )

    
    @classmethod
    def basic_drivers_license(
        cls , number:int=None , dob:str=None , 
        first_name:str=None, last_name:str=None):
        """
        Verify drivers license
        
        Args:
            number : license number
            dob : date of birth
            first_name : first name
            last_name : last name
        Returns : 
            Json data from Prembly API.
        """
        #AAD23208212298
        #1999-12-21
        #test
        #test
        data = {
            'number': number , 'dob' : dob, 
            'first_name' : first_name, 'last_name' : last_name
        }
        url = cls.create_request_url(suburl='/drivers_license/basic') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def advance_drivers_license(
        cls , number:int=None , dob:str=None , 
        first_name:str=None, last_name:str=None):
        """
        Verify drivers license
        
        Args:
            number : license number
            dob : date of birth
            first_name : first name
            last_name : last name
        Returns : 
            Json data from Prembly API.
        NOTE : dob format should look like 1998-06-19 - Format)
        """
        #AAD23208212298
        #1999-12-21
        #test
        #test
        data = {'number': number , 'dob' : dob, 
                'first_name' : first_name, 'last_name' : last_name
                }
        url = cls.create_request_url(suburl='/drivers_license/advance') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def image_drivers_license(cls ,  image:str=None):
        """
        Verify drivers license ID image
        
        Args:
            image : License image
        Returns : 
            Json data from Prembly API.
        """        
        data  = {'image' : image }
        url = cls.create_request_url(suburl='/drivers_license/image') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def image_drivers_license_verification(cls , number:int=None,  dob:str=None ,  image:str=None):
        """
        Verify drivers license ID image
        
        Args:
            number : FRSC number
            dob : date of birth
            image : image(png,jpg, base64)
        Returns : 
            Json data from Prembly API.
        """        
        data  = {'image' : image , 'number': number , 'dob' : dob,  }
        url = cls.create_request_url(suburl='/drivers_license_with_face') 
        return cls._handle_request('POST', url , data=data )


    @classmethod
    def international_passport(cls , number:int=None,  last_name:str=None):
        """
        Verify international passport
        
        Args:
            number : passport number
            last_name : user's last name
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 'number': number , 'last_name' : last_name,  }
        url = cls.create_request_url(suburl='/national_passport') 
        return cls._handle_request('POST', url , data=data )


    @classmethod
    def international_passport_image(cls , image:str=None,  customer_reference:str=None , customer_name:str=None):
        """
        Verify international passport image 
        
        Args:
            customer_reference : unique customer reference
            customer_name : customer name
            image : passport image(png,jpg, base64)
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 'image': image , 'customer_reference' : customer_reference,'customer_name' : customer_name,  }
        url = cls.create_request_url(suburl='/national_passport_image') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def international_passport_with_face(cls , image:str=None,  last_name:str=None , number:int=None):
        """
        Verify international passport image 
        
        Args:
            last_name : user's last name
            number : passport number
            image :  image(png,jpg, base64)
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 'image': image , 'last_name' : last_name,'number' : number,  }
        url = cls.create_request_url(suburl='/national_passport_with_face') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def international_passport_async(cls , last_name:str=None , number:int=None):
        """
        Verify international passport in an asynchronous manner. The passport details will be verified and send later to your webhook url
        NOTE : configure your webhook URL before using this function
        
        Args:
            last_name : user's last name
            number : passport number
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 'last_name' : last_name,'number' : number,  }
        url = cls.create_request_url(suburl='/national_passport/async') 
        return cls._handle_request('POST', url , data=data )


    @classmethod
    def credit_bureau(
        cls, customer_reference, 
        customer_name:str=None , number:int=None, mode:str=None , dob:str=None
        ):
        """
        Verify advance credit details of a user
        
        Args:
            customer_reference : unique customer reference
            customer_name : customer name
            number : if model is ID(should be BVN)
            dob : if model is BIO(Date of birth)
            mode : either ID or BVN
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 
            'customer_name' : customer_name, 
            'customer_reference' : customer_reference ,
            'number' : number,  'dob': dob  , 'mode' : mode
        }
        url = cls.create_request_url(suburl='/credit_bureau/customer/advance') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def credit_bureau_commercial(
        cls, customer_reference, 
        customer_name:str=None , rc_number:int=None
        ):
        """
        Verify advance credit details of a business
        
        Args:
            rc_number : company RC number
            customer_name : customer  name
            customer_reference : unique customer reference
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 
            'customer_name' : customer_name, 
            'customer_reference' : customer_reference ,
            'rc_number' : rc_number
        }
        url = cls.create_request_url(suburl='/credit_bureau/commercial/advance') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def credit_bureau_commercial_basic(
        cls,customer_name:str=None , rc_number:int=None ):
        """
        Verify basic credit details of a business
        
        Args:
            rc_number : company RC number
            customer_name : customer  name
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 
            'customer_name' : customer_name, 
            'rc_number' : rc_number
        }
        url = cls.create_request_url(suburl='/credit_bureau/commercial/basic') 
        return cls._handle_request('POST', url , data=data )

    @classmethod
    def credit_bureau_statement(
        cls,first_name:str=None ,phone_number:int=None ):
        """
        Verify basic credit details of a business
        
        Args:
            phone_number : Phone number
            first_name : first name
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 
            'first_name' : first_name, 
            'phone_number' : phone_number
        }
        url = cls.create_request_url(suburl='/credit_bureau/commercial/basic') 
        return cls._handle_request('POST', url , data=data )


    @classmethod
    def nin_slip(cls, image: str = None) :
        """
        Verify a National Identification Number(NIN) Slip
        
        Args:
            image : Nin slip image
        Returns : 
            Json data from Prembly API.
        """
        url = cls.create_request_url(suburl='/biometrics/merchant/data/verification/nin/image') 

        return cls._handle_request('POST', url , data=image)




    @classmethod
    def nin_lookup(cls, number=None , number_nin=None) :
        """
        Verify a National Identification Number(NIN) with phone number and (NIN) number
        
        Args:
            number : Phone number used for nin registration
            number_nin : Nin registration number
        Returns : 
            Json data from Prembly API.
        """
        data = {'number': number ,'number_nin': number_nin } 
        
        url = cls.create_request_url(suburl='/biometrics/merchant/data/verification/nin_wo_face') 

        return cls._handle_request('POST', url , data=data)


    @classmethod
    def nin_virtual(cls, number=None , number_nin=None) :
        """
        Verify a National Identification Number(NIN) with NIN and virtual number
        
        Args:
            number : Virtual nin number
            number_nin : Nin registration number
        Returns : 
            Json data from Prembly API. 
        Note:
            The Virtual NIN (vNIN) is designed to replace the raw 11-digit NIN for everyday usage.
            Where until now, the raw NIN had been shared and stored by various entities mostly without the knowledge (or consent) of the ID Holder or the Custodian of Identity in Nigeria, the NIMC.\n
            Virtual NIN consists of 16 alpha-numeric characters that can be generated using:\n
            NIMC official mobile app\n
            USSD - _346_3_customer NIN_696739#\n
            Identitypass Short Code: 696739
            
        """
        data = {'number': number ,'number_nin': number_nin } 
        url = cls.create_request_url(suburl='/biometrics/merchant/data/verification/nin_wo_face') 
        return cls._handle_request('POST', url , data=data)


    @classmethod
    def nin_face(cls, number=None , image: str =None) :
        """
        Verify a National Identification Number(NIN) with user's image

        Args:
            number : Virtual nin number
            image : Image url 
        Returns : 
            Json data from Prembly API.
        """
        data = {'number': number , 'image': image}
        # image = open('image','rb').read()
        # data.update({'image': image} ) 
            
        url = create_request_url(subsuburl='/biometrics/merchant/data/verification/nin') 
        return cls._handle_request('POST', url , data=data)







m = Verification.bank_account_with_name()