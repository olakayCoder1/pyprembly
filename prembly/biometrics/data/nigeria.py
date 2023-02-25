from prembly.base import PremblyBase
from prembly.exceptions import *
from prembly.utils import create_request_url



class DataVerification(PremblyBase):
    """
    Base class for all IdentityPass API available in Nigeria
    """
    
    def cac(self, rc_number: int = None , company_type : str ='RC' ):
        """
        Verify a business using rc_number
        
        Params:
            rc_number : The registration number of company

            company_type : company type : default - > RC
        Returns : 
            Json data from Prembly API.
        """
        data = {'company_type': company_type , 'rc_number': rc_number}
        url = self.create_request_url(suburl='/cac') 
        return self._handle_request('POST', url , data=data)


    def cac_with_name(self,company_name : str = None ):
        """
        Verify a business using rc_number
        company_name : The company name
        Params:
            company_name : The company name
        Returns : 
            Json data from Prembly API.
        """
        # 092932
        # TEST COMPANY
        data = {'company_type': company_name ,'company_name': company_name}
        verify_url = self._BASE_END_POINT_VERSION + '/cac_w_name'
        url = self.create_request_url(suburl=verify_url) 
        return self._handle_request('POST', url , data=data)


    
    def cac_advance(self,  rc_number: int = None ,  company_type : str ='RC' , company_name : str = None ):
        """
        Verify a business using rc_number
        
        Params:
            rc_number : The registration number of company

            company_type : company type : default - > RC
            company_name : The company name
        Returns : 
            Json data from Prembly API.
        """
        # 092932
        # TEST COMPANY
        data = {'company_type': company_type , 'rc_number': rc_number , 'company_name': company_name }
        url = self.create_request_url(suburl='/cac/advance') 
        return self._handle_request('POST', url , data=data)


    def bvn_number(self, number: int = None ):
        """
        Verify a Bank Verification Number (BVN)
        number : Bank Verification Number
        Params:
            number : Bank Verification Number
        Returns : 
            Json data from Prembly API.
        """
        data = { 'number': number }
        url = self.create_request_url(suburl='/bvn') 
        return self._handle_request('POST', url , data=data)


    def bvn_with_face(self, number: int = None , image: str = None ):
        """
        Verify a Bank Verification Number (BVN) using image and number
       
        Params:
            number : Bank Verification Number
            image : Image url(png, jpeg , base64)
        Returns : 
            Json data from Prembly API.
        """
        data = { 'image': image , 'number': number  }
        url = self.create_request_url(suburl='/bvn_w_face') 
        return self._handle_request('POST', url , data=data)

    
    def phone_number(self, number: int = None , v_type:str='normal'):
        """
        Verify a Phone Number
        
        Params:
            number : Phone number

            v_type : Phone number verification type eg advance or normal : default - > normal
        Returns : 
            Json data from Prembly API.
        """
        data = {'number': number }
        url = self.create_request_url(suburl='/phone_number') 
        return self._handle_request('POST', url , data=data)


    def banks_code(self):
        """
        Get all banks code
        """
        url = self.create_request_url(suburl='/bank_code') 
        return self._handle_request('GET', url )


    def bank_account(self , number:int=None,bank_code:str=None):
        """
        Verify bank account number
        
        Params:
            number : bank account number
            bank_code : code of the user's bank
        Returns : 
            Json data from Prembly API.
        """
        data = {
                'bank_code': bank_code ,  'number': number
            }
        url = self.create_request_url(suburl='/bank_account') 
        return self._handle_request('POST', url , data=data )
    


    def all_bank_with_statement(self ):
        """
        Get all available banking institution that bank statement can be retrieve
        """
        url = self.create_request_url(suburl='/bank_statement/institutions') 
        return self._handle_request('GET', url )
    

    # def bank_statement(self ):
    #     """
    #     Get all available banking institution that bank statement can be retrieve
    #     """
    #     url = self.create_request_url(suburl='/bank_statement') 
    #     return self._handle_request('POST', url )

    
    def advance_bank_account(self , number:int=None,bank_code:str=None):
        """
        Verify bank account number
        
        Params:
            number : bank account number
            bank_code : code of the user's bank
        Returns : 
            Json data from Prembly API.
        """
        data = {'bank_code': bank_code ,  'number': number}
        url = self.create_request_url(suburl='/bank_account/advance') 
        return self._handle_request('POST', url , data=data )


    def bank_account_with_name(
        self , number:int=None,bank_code:str=None , 
        customer_name:str=None , customer_reference:str=None):
        """
        Verify bank account number
        
        Params:
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
        url = self.create_request_url(suburl='/bank_account/comparism') 
        return self._handle_request('POST', url , data=data )



    def voters_card_image(self , image:str=None):
        """
        Verify voters card ID image
        
        Params:
            image : voters card image(png,jpg, base64)
        Returns : 
            Json data from Prembly API.
        """
        data = {'image': image }
        url = self.create_request_url(suburl='/voters_card/image') 
        return self._handle_request('POST', url , data=data )

    
    def voters_card_lookup(self , number:int=None , state:str=None , last_name:str=None):
        """
        Verify voters card number
        
        Params:
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
        url = self.create_request_url(suburl='/voters_card') 
        return self._handle_request('POST', url , data=data )

    

    def basic_drivers_license(
        self , number:int=None , dob:str=None , 
        first_name:str=None, last_name:str=None):
        """
        Verify drivers license
        
        Params:
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
        url = self.create_request_url(suburl='/drivers_license/basic') 
        return self._handle_request('POST', url , data=data )


    def advance_drivers_license(
        self , number:int=None , dob:str=None , 
        first_name:str=None, last_name:str=None):
        """
        Verify drivers license
        
        Params:
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
        url = self.create_request_url(suburl='/drivers_license/advance') 
        return self._handle_request('POST', url , data=data )


    def image_drivers_license(self ,  image:str=None):
        """
        Verify drivers license ID image
        
        Params:
            image : License image
        Returns : 
            Json data from Prembly API.
        """        
        data  = {'image' : image }
        url = self.create_request_url(suburl='/drivers_license/image') 
        return self._handle_request('POST', url , data=data )


    def image_drivers_license_verification(self , number:int=None,  dob:str=None ,  image:str=None):
        """
        Verify drivers license ID image
        
        Params:
            number : FRSC number
            dob : date of birth
            image : image(png,jpg, base64)
        Returns : 
            Json data from Prembly API.
        """        
        data  = {'image' : image , 'number': number , 'dob' : dob,  }
        url = self.create_request_url(suburl='/drivers_license_with_face') 
        return self._handle_request('POST', url , data=data )


    
    def international_passport(self , number:int=None,  last_name:str=None):
        """
        Verify international passport
        
        Params:
            number : passport number
            last_name : user's last name
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 'number': number , 'last_name' : last_name,  }
        url = self.create_request_url(suburl='/national_passport') 
        return self._handle_request('POST', url , data=data )


    
    def international_passport_image(self , image:str=None,  customer_reference:str=None , customer_name:str=None):
        """
        Verify international passport image 
        
        Params:
            customer_reference : unique customer reference
            customer_name : customer name
            image : passport image(png,jpg, base64)
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 'image': image , 'customer_reference' : customer_reference,'customer_name' : customer_name,  }
        url = self.create_request_url(suburl='/national_passport_image') 
        return self._handle_request('POST', url , data=data )


    def international_passport_with_face(self , image:str=None,  last_name:str=None , number:int=None):
        """
        Verify international passport image 
        
        Params:
            last_name : user's last name
            number : passport number
            image :  image(png,jpg, base64)
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 'image': image , 'last_name' : last_name,'number' : number,  }
        url = self.create_request_url(suburl='/national_passport_with_face') 
        return self._handle_request('POST', url , data=data )


    def international_passport_async(self , last_name:str=None , number:int=None):
        """
        Verify international passport in an asynchronous manner. The passport details will be verified and send later to your webhook url
        NOTE : configure your webhook URL before using this function
        
        Params:
            last_name : user's last name
            number : passport number
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 'last_name' : last_name,'number' : number,  }
        url = self.create_request_url(suburl='/national_passport/async') 
        return self._handle_request('POST', url , data=data )


    
    def credit_bureau(
        self, customer_reference, 
        customer_name:str=None , number:int=None, mode:str=None , dob:str=None
        ):
        """
        Verify advance credit details of a user
        
        Params:
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
        url = self.create_request_url(suburl='/credit_bureau/customer/advance') 
        return self._handle_request('POST', url , data=data )

    
    def credit_bureau_commercial(
        self, customer_reference, 
        customer_name:str=None , rc_number:int=None
        ):
        """
        Verify advance credit details of a business
        
        Params:
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
        url = self.create_request_url(suburl='/credit_bureau/commercial/advance') 
        return self._handle_request('POST', url , data=data )


    def credit_bureau_commercial_basic(
        self,customer_name:str=None , rc_number:int=None ):
        """
        Verify basic credit details of a business
        
        Params:
            rc_number : company RC number
            customer_name : customer  name
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 
            'customer_name' : customer_name, 
            'rc_number' : rc_number
        }
        url = self.create_request_url(suburl='/credit_bureau/commercial/basic') 
        return self._handle_request('POST', url , data=data )


    def credit_bureau_statement(
        self,first_name:str=None ,phone_number:int=None ):
        """
        Verify basic credit details of a business
        
        Params:
            phone_number : Phone number
            first_name : first name
        Returns : 
            Json data from Prembly API.
        """        
        data  = { 
            'first_name' : first_name, 
            'phone_number' : phone_number
        }
        url = self.create_request_url(suburl='/credit_bureau/commercial/basic') 
        return self._handle_request('POST', url , data=data )



    def nin_slip(self, image: str = None) :
        """
        Verify a National Identification Number(NIN) Slip
        
        Params:
            image : Nin slip image
        Returns : 
            Json data from Prembly API.
        """
        url = self.create_request_url(suburl='/biometrics/merchant/data/verification/nin/image') 

        return self._handle_request('POST', url , data=image)





    def nin_lookup(self, number=None , number_nin=None) :
        """
        Verify a National Identification Number(NIN) with phone number and (NIN) number
        
        Params:
            number : Phone number used for nin registration
            number_nin : Nin registration number
        Returns : 
            Json data from Prembly API.
        """
        data = {'number': number ,'number_nin': number_nin } 
        
        url = self.create_request_url(suburl='/biometrics/merchant/data/verification/nin_wo_face') 

        return self._handle_request('POST', url , data=data)



    def nin_virtual(self, number=None , number_nin=None) :
        """
        Verify a National Identification Number(NIN) with NIN and virtual number
        
        Params:
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
        url = self.create_request_url(suburl='/biometrics/merchant/data/verification/nin_wo_face') 
        return self._handle_request('POST', url , data=data)


    
    def nin_face(self, number=None , image: str =None) :
        """
        Verify a National Identification Number(NIN) with user's image

        Params:
            number : Virtual nin number
            image : Image url 
        Returns : 
            Json data from Prembly API.
        """
        data = {'number': number , 'image': image}
        # image = open('image','rb').read()
        # data.update({'image': image} ) 
            
        url = create_request_url(subsuburl='/biometrics/merchant/data/verification/nin') 
        return self._handle_request('POST', url , data=data)







