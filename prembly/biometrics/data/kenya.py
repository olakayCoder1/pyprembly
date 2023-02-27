from prembly.base import PremblyBase
from prembly.utils import create_request_url


class DataVerification(PremblyBase):
    """
    Base class for all IdentityPass API available in Kenya
    """

    def passport(
            self, 
            number:int=None , 
            customer_name:str=None , 
            customer_reference:int=None
            ):
        """
        Verify user passport
        
        Params:
            number : passport number
            customer_name : Customer name
            customer_reference : Customer reference
        Returns : 
            Json data from Prembly API.
        """

        data = {
            'number' :number,
            'customer_name': customer_name ,
            'customer_reference': customer_reference
        }
        url = self.create_request_url(suburl='/ke/passport') 
        return self._handle_request('POST', url , data=data)



    def drivers_license(
            self ,  
            number:int=None ,
            customer_name:str=None , 
            customer_reference:int=None
            ):
        """
        Verify user drivers license
        
        Params:
            number : license number
            customer_name : Customer name
            customer_reference : Customer reference
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
            'customer_name': customer_name ,
            'customer_reference': customer_reference
        }
        url = self.create_request_url(suburl='/ke/drivers_license') 
        return self._handle_request('POST', url , data=data)