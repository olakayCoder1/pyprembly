from prembly.base import BaseConfig
from prembly.utils import create_request_url


class Verification(BaseConfig):
    """
    Base class for all IdentityPass API available in Kenya
    """

    def passport(self, number:int=None , customer_name:str=None , customer_reference:int=None):

        data = {
            'number' :number,
            'customer_name': customer_name ,
            'customer_reference': customer_reference
        }
        url = self.create_request_url(suburl='/ke/passport') 
        return self._handle_request('POST', url , data=data)



    def drivers(self ,  number:int=None , customer_name:str=None , customer_reference:int=None):
        data = {
            'number' :number,
            'customer_name': customer_name ,
            'customer_reference': customer_reference
        }
        url = self.create_request_url(suburl='/ke/drivers_license') 
        return self._handle_request('POST', url , data=data)