from pyprembly.base import PremblyBase


class DataVerification(PremblyBase):
    """
    Base class for all IdentityPass API available in Ghana
    """


    def drivers_license(self ,  number  , dob=None):
        """
        Verify user drivers license
        
        Params:
            number : License number
            dob : date of birth[yyyy-mm-dd]
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
            'dob': dob ,
        }
        url = self.create_request_url(suburl='/gh/drivers_license') 
        return self._handle_request('POST', url , data=data)


    def ssnit(self ,  number  ):
        """
        Verify user Social Security and National Insurance Trust(SSNIT)
        
        Params:
            number : SSNIT number
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
        }
        url = self.create_request_url(suburl='/gh/ssnit') 
        return self._handle_request('POST', url , data=data)


    def ssnit_with_face(self ,  number=None, image=None  ):
        """
        Verify user Social Security and National Insurance Trust(SSNIT) number with uploaded image
        
        Params:
            number : SSNIT number
            image : face image(base64, png, jpg )
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
            'image' :image,
        }
        url = self.create_request_url(suburl='/gh/ssnit/face') 
        return self._handle_request('POST', url , data=data)


    def voters_card(self, number=None , type='MAIN' ):
        """
        Verify voters card
        
        Params:
            number : Voters card number
            type :  Voters card type [ MAIN or OLD ] default MAIN
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' : number,
            'type' : type.upper(),
        }
        url = self.create_request_url(suburl='/gh/voters') 
        return self._handle_request('POST', url , data=data)


    def international_passport(self, number=None ):
        """
        Verify user passport
        number : Passport number
        Params:
            number : Passport number
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' : number,
        }
        url = self.create_request_url(suburl='/gh/passport') 
        return self._handle_request('POST', url , data=data)



