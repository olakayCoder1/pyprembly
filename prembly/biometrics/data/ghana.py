from prembly.base import PremblyBase
from prembly.utils import create_request_url


class DataVerification(PremblyBase):
    """
    Base class for all IdentityPass API available in Ghana
    """


    def drivers_license(self ,  number  , dob:str=None):
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
        Verify user SSNIT
        
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


    def voters_card(self, number:int=None , type:str='MAIN' ):
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


    def international_passport(self, number:int=None ):
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



