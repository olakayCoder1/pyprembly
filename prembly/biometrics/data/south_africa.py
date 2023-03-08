from prembly.base import PremblyBase
from prembly.utils import create_request_url


class DataVerification(PremblyBase):
    """
    Base class for all IdentityPass API available in South Africa
    """ 

    def national_id(
            self , 
            firstname:str=None, 
            lastname:str= None , 
            nationalid:str=None , 
            dob:str=None
            ):
        """
        Verify user national id card
        
        Params:
            firstname : user first name
            lastname : user first name
            nationalid : id card unique identifier
            dob :  user date of birth
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'firstname' :firstname,
            'lastname' :lastname,
            'nationalid' :nationalid,
            'dob': dob ,
        }
        url = self.create_request_url(suburl='/sa/national_id') 
        return self._handle_request('POST', url , data=data)


    def company(self , customer_reference:str=None, customer_name:str= None , reg_number:str=None):
        """
        Verify business
        
        Params:
            customer_reference :your customer reference
            customer_name : your customer name
            reg_number : business or company registration number
            dob :  user date of birth
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'customer_reference' :customer_reference,
            'customer_name' :customer_name,
            'reg_number' :reg_number,
        }
        url = self.create_request_url(suburl='/sa/company') 
        return self._handle_request('POST', url , data=data)


