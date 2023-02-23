from prembly.base import BaseConfig
from prembly.utils import create_request_url



class Search(BaseConfig):

    def search_with_email(self , email ):
        """
        Verify a company using email
        email : Company email    
            
        """
        data = {
            'email' :email,
        }
        verify_url = self._BASE_END_POINT_VERSION + '/global/company/search_with_email'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data)


    def search_with_name(self , country_code:str=None , company_name:str=None ):
        """
        Verify a company using  name
        country_code : country code eg Nigeria ng
        company_name : company registration name    
            
        """
        data = {
            'country_code' :country_code.lower(),
            'company_name' :company_name,
        }
        verify_url = self._BASE_END_POINT_VERSION + '/global/company/search_with_name'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data)


    def search_with_string(self , query:str=None , customer_name:str=None, customer_reference:str=None ):
        """
        Verify a company
        query : Search query
        customer_name : customer name 
        customer_reference: customer reference  
            
        """
        data = {
            'query' :query,
            'customer_name' :customer_name,
            'customer_reference' :customer_reference,
        }
        verify_url = self._BASE_END_POINT_VERSION + '/global/company/search_with_string'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data)


    def search_with_number(
        self ,customer_name:str=None, customer_reference:str=None ,
        country_code:str=None , company_number:str=None ):
        """
        Verify a company
        customer_name : customer name 
        customer_reference: customer reference  
        country_code: company country code ge NG 
        company_number: company registration number ge RC-000000 
            
        """
        data = {
            'customer_name' :customer_name,
            'customer_reference' :customer_reference,
            'country_code' :country_code,
            'company_number' :company_number,
        }
        verify_url = self._BASE_END_POINT_VERSION + '/global/company'
        url = create_request_url(url=verify_url) 
        return self._handle_request('POST', url , data=data) 